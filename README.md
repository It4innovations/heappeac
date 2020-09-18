<img align="right" width="35%" src="docs/imgs/logo.png?sanitize=true">

# HEAppEAC - HEAppE API Python client

A Python client for [Heappe](heappe.eu).

## Example usage

```
import json
import os
import time
from io import StringIO

import paramiko
from paramiko import SSHClient
from scp import SCPClient

import heappeac as hp

username = ""
password = ""

configuration = hp.Configuration()
api_instance = hp.ApiClient(configuration)

print(f"Authenticating {username}...")
cred = {
    "_preload_content": False,
    "body": {
        "credentials": {
            "password": password,
            "username": username
        }
    }
}
ulm = hp.api.UserAndLimitationManagementApi(api_instance)
r = ulm.authenticate_user_password(**cred)
session_code = json.loads(r.data)
print(f"Session code: {session_code}")


print("Fetching cluster info...")
lac_body = {
    "_preload_content": False,
}
ci = hp.api.ClusterInformationApi(api_instance)
r = ci.list_available_clusters(**lac_body)
r_data = json.loads(r.data)
print(r_data)


print("Creating job template...")
jm = hp.api.JobManagementApi(api_instance)
job_spec_body = {
    "_preload_content": False,
    "body": {
        "jobSpecification": {
            "name": "my_job",
            "minCores": 1,
            "maxCores": 24,
            "priority": 4,
            "project": "test_project", #
            "waitingLimit": 0,
            "walltimeLimit": 600,
            "clusterNodeTypeId": 7,
            "environmentVariables": [],
            "tasks": [
                {
                    "name": "my_job",
                    "minCores": 1,
                    "maxCores": 24,
                    "walltimeLimit": 600,
                    "standardOutputFile": "stdout",
                    "standardErrorFile": "stderr",
                    "progressFile": "stdprog",
                    "logFile": "stdlog",
                    "commandTemplateId": 2,
                    "environmentVariables": [],
                    "dependsOn": [],
                    "templateParameterValues": [
                        {
                            "commandParameterIdentifier": "inputParam",
                            "parameterValue": "test"
                        }
                    ]
                }
            ]
        },
        "sessionCode": session_code
    }
}
r = jm.create_job(**job_spec_body)
r_data = json.loads(r.data)
job_id = r_data["id"]
print(f"Job ID: {job_id}")


print(f"Submitting job {job_id}...")
submit_body = {
    "_preload_content": False,
    "body":
        {
            "createdJobInfoId": job_id,
            "sessionCode": session_code
        }
}
r = jm.submit_job(**submit_body)
r_data = json.loads(r.data)


print(f"Waiting for job {job_id} to finish...")
gcji_body = {
    "_preload_content": False,
    "body": {
        "submittedJobInfoId": job_id,
        "sessionCode": session_code
    }
}

while True:
    r = jm.get_current_info_for_job(**gcji_body)
    r_data = json.loads(r.data)
    state = r_data["state"]
    # State codes: https://code.it4i.cz/ADAS/HEAppE/Middleware/-/blob/new_master/ServiceTier/EtchProxy
    # /EtchServiceTier.etch#L117
    if r_data["state"] > 8:
        print(f"The job has finished with state {state}")
        break
    print(f"Waiting for job {job_id} to finish... current state: {state}")
    time.sleep(5)


print("Fetching logs...")
ft = hp.api.FileTransferApi(api_instance)
ft_body = {
    "_preload_content": False,
    "body": {
        "submittedJobInfoId": job_id,
        "sessionCode": session_code
    }
}
r = ft.get_file_transfer_method(**ft_body)
r_data = json.loads(r.data)

ssh = SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_username = r_data["credentials"]["username"]
pkey_file = StringIO(r_data["credentials"]["privateKey"])
pkey = paramiko.rsakey.RSAKey.from_private_key(pkey_file)
ssh.connect(r_data["serverHostname"], username=ssh_username, pkey=pkey)
base_path = r_data["sharedBasepath"]
filenames = ["stdout", "stderr"]
with SCPClient(ssh.get_transport()) as scp:
    [scp.get(os.path.join(base_path, fn), fn) for fn in filenames]

ft_body = {
    "_preload_content": False,
    "body": {
        "submittedJobInfoId": job_id,
        "usedTransferMethod": r_data,
        "sessionCode": session_code
    }
}
r = ft.end_file_transfer(**ft_body)
r_data = json.loads(r.data)
print(", ".join(filenames) + " fetched")


print("Fetching resource usage report...")
jr = hp.api.JobReportingApi(api_instance)
rur_body = {
    "_preload_content": False,
    "body": {
        "JobId": job_id,
        "sessionCode": session_code
    }
}
r = jr.get_resource_usage_report_for_job(**rur_body)
r_data = json.loads(r.data)
print("Done.")

```

## Acknowledgement

This project has received funding from the programme
"Support for Science and Research in the Moravian-Silesian Region" (RRC/10/2017).

![MSK Logo](docs/imgs/logo_msk.png?raw=true)