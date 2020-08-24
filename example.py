import heappeac as sc
import json
import time


username = ""
password = ""

configuration = sc.Configuration()
api_instance = sc.ApiClient(configuration)

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
ulm = sc.api.UserAndLimitationManagementApi(api_instance)
r = ulm.authenticate_user_password(**cred)
session_code = json.loads(r.data)
print(f"Session code: {session_code}")


print("Fetching cluster info...")
lac_body = {
    "_preload_content": False,
}
ci = sc.api.ClusterInformationApi(api_instance)
r = ci.list_available_clusters(**lac_body)
r_data = json.loads(r.data)
print(r_data)


print("Creating job template...")
jm = sc.api.JobManagementApi(api_instance)
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
                    "clusterTaskSubdirectory": "string",
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
