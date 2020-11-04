import json
import os
import time
from io import StringIO
from pathlib import Path

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
        "Credentials": {
            "Password": password,
            "Username": username
        }
    }
}
ulm = hp.api.UserAndLimitationManagementApi(api_instance)
r = ulm.heappe_user_and_limitation_management_authenticate_user_password_post(**cred)
session_code = json.loads(r.data)
print(f"Session code: {session_code}")


print("Fetching cluster info...")
lac_body = {
    "_preload_content": False,
}
ci = hp.api.ClusterInformationApi(api_instance)
r = ci.heappe_cluster_information_list_available_clusters_get(**lac_body)
r_data = json.loads(r.data)
print(r_data)


print("Creating job template...")
jm = hp.api.JobManagementApi(api_instance)

job_spec_body = {
    "_preload_content": False,
    "body": {
        "JobSpecification": {
        "Name": "my_job",
        #"Project": "test_project",
        #"WaitingLimit": 0,
        #"NotificationEmail": "string",
        #"PhoneNumber": "string",
        #"NotifyOnAbort": true,
        #"NotifyOnFinish": true,
        #"NotifyOnStart": true,
        "ClusterId": 2,
        "FileTransferMethodId": 2,
        "EnvironmentVariables": [],
        "Tasks": [
            {
                "Name": "task_1",
                "MinCores": 1,
                "MaxCores": 24,
                "WalltimeLimit": 600,
                #"RequiredNodes": "string",
                "Priority": 4,
                #"JobArrays": "string",
                #"IsExclusive": true,
                #"IsRerunnable": true,
                #"StandardInputFile": "string",
                "StandardOutputFile": "stdout",
                "StandardErrorFile": "stderr",
                "ProgressFile": "stdprog",
                "LogFile": "stdlog",
                #"ClusterTaskSubdirectory": "string",
                "ClusterNodeTypeId": 8,
                "CommandTemplateId": 2,
                #"CpuHyperThreading": true,
                "EnvironmentVariables": [],
                #"DependsOn": [],
                "TemplateParameterValues": [
                    {
                        "CommandParameterIdentifier": "inputParam",
                        "ParameterValue": "test"
                    }
                ]
            }
        ]
        },
        "SessionCode": session_code
    }
}
r = jm.heappe_job_management_create_job_post(**job_spec_body)
r_data = json.loads(r.data)
job_id = r_data["Id"]
tasks = r_data["Tasks"]
print(f"Job ID: {job_id}")


print(f"Submitting job {job_id}...")
submit_body = {
    "_preload_content": False,
    "body":
        {
            "CreatedJobInfoId": job_id,
            "SessionCode": session_code
        }
}
r = jm.heappe_job_management_submit_job_post(**submit_body)
r_data = json.loads(r.data)


print(f"Waiting for job {job_id} to finish...")
gcji_body = {
    "_preload_content": False,
    "body": {
        "SubmittedJobInfoId": job_id,
        "SessionCode": session_code
    }
}

while True:
    r = jm.heappe_job_management_get_current_info_for_job_post(**gcji_body)
    r_data = json.loads(r.data)
    state = r_data["State"]
    # State codes: https://code.it4i.cz/ADAS/HEAppE/Middleware/-/blob/new_master/ServiceTier/EtchProxy
    # /EtchServiceTier.etch#L117
    if r_data["State"] > 8:
        print(f"The job has finished with state {state}")
        break
    print(f"Waiting for job {job_id} to finish... current state: {state}")
    time.sleep(30)


print("Fetching logs...")
ft = hp.api.FileTransferApi(api_instance)
ft_body = {
    "_preload_content": False,
    "body": {
        "SubmittedJobInfoId": job_id,
        "SessionCode": session_code
    }
}
r = ft.heappe_file_transfer_get_file_transfer_method_post(**ft_body)
r_data = json.loads(r.data)

r = ft.heappe_file_transfer_list_changed_files_for_job_post(**ft_body)
filenames = [os.path.normpath(path) for path in json.loads(r.data)]

print(f"Files changed during job execution: {filenames}")

print("Fetching the files...")
ssh = SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_username = r_data["Credentials"]["UserName"]
pkey_file = StringIO(r_data["Credentials"]["PrivateKey"])
pkey = paramiko.rsakey.RSAKey.from_private_key(pkey_file)
ssh.connect(r_data["ServerHostname"], username=ssh_username, pkey=pkey)
base_path = r_data["SharedBasepath"]
with SCPClient(ssh.get_transport()) as scp:
    for fn in filenames:
        Path(os.path.dirname(fn)).mkdir(parents=True, exist_ok=True)
        scp.get(os.path.join(base_path, fn), fn)

ft_body = {
    "_preload_content": False,
    "body": {
        "SubmittedJobInfoId": job_id,
        "UsedTransferMethod": r_data,
        "SessionCode": session_code
    }
}
r = ft.heappe_file_transfer_end_file_transfer_post(**ft_body)
r_data = json.loads(r.data)
print(", ".join(filenames) + " fetched")


print("Fetching resource usage report...")
jr = hp.api.JobReportingApi(api_instance)
rur_body = {
    "_preload_content": False,
    "body": {
        "JobId": job_id,
        "SessionCode": session_code
    }
}
r = jr.heappe_job_reporting_get_resource_usage_report_for_job_post(**rur_body)
r_data = json.loads(r.data)
print("Done.")

# Remove job after execution on HPC Cluster
print(f"Removing job {job_id}...")
ft_body = {
    "_preload_content": False,
    "body": {
        "SubmittedJobInfoId": job_id,
        "SessionCode": session_code
    }
}
r = jm.heappe_job_management_delete_job_post(**ft_body)
r_data = json.loads(r.data)
print(r_data)
