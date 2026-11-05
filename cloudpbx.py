import requests


baseURL = "https://ycm.yeastar.com"



def queryCloudPBXs(access_token, pageSize=10, pageNumber=1, sort="createTime", search="", userId=""):
    path = "/dm/open_api/v2/cloud_pbx/instances"
    # Argument Validation:
    if 1 <= pageSize < 50:
        pass
    else:
        raise ValueError("Page size must be between 1 and 50 (Default: 10)")

    validSortOptions = {
        "cloudPbxId",
        "-cloudPbxId",
        "createTime",
        "-createTime"
    }

    if sort not in validSortOptions:
        raise ValueError("Sort method must be one of the following:\ncloudPbxId\n-cloudPbxId\ncreateTime\n-createTime")
    else:
        pass

    # Build basic parameters
    parameters = f"?pageSize={pageSize}&pageNumber={pageNumber}&sort={sort}&userId={userId}"

    # If search keyword is present, append to parameters
    if search != "":
        parameters += f"&search={search}"
    
    response = requests.get(f"{baseURL}{path}{parameters}", headers={'Authorization': f'Bearer {access_token}'})
    try:
        return response.json()['data']
    except:
        raise Exception(f"Error:\n{response.json()}")

def queryPbxByID(access_token, cloudPbxId):
    path = f"/dm/open_api/v1/cloud_pbx/instances/{cloudPbxId}"

    response = requests.get(f"{baseURL}{path}", headers={"Authorization": f"Bearer {access_token}"})

    try:
        return response.json()['data']
    except:
        raise Exception(f"Error:\n{response.json()}")

def queryPbxByURL(access_token, url):
    path = f"/dm/open_api/v1/cloud_pbx/instances/get"

    response = requests.get(f"{baseURL}{path}?url={url}", headers={"Authorization": f"Bearer {access_token}"})

    try:
        return response.json()['data']
    except:
        raise Exception(f"Error:\n{response.json()}")

def queryCloudPbxStatus(access_token, cloudPbxId):
    path = f"/dm/open_api/v1/cloud_pbx/instances/{cloudPbxId}/status"

    response = requests.get(f"{baseURL}{path}", headers={"Authorization": f"Bearer {access_token}"})

    try:
        return response.json()['data']
    except:
        raise Exception(f"Error:\n{response.json()}")
    
def getCloudPbxActivationInfo(access_token, cloudPbxId):
    path = f"/dm/open_api/v1/cloud_pbx/instances/{cloudPbxId}/activation_info"

    response = requests.get(f"{baseURL}{path}", headers={"Authorization": f"Bearer {access_token}"})

    try:
        return response.json()['data']
    except:
        raise Exception(f"Error:\n{response.json()}")

def queryPbxAssignedTrunks(access_token, cloudPbxId):
    path = "/dm/open_api/v1/shared_trunk/pbx/used"

    response = requests.get(f"{baseURL}{path}?cloudPbxId={cloudPbxId}", headers={"Authorization": f"Bearer {access_token}"})

    try:
        return response.json()['data']
    except:
        raise Exception(f"Error:\n{response.json()}")

def queryPbxAssignedDIDs(access_token, cloudPbxId):
    path = f"/dm/open_api/v1/did_management/{cloudPbxId}/did"

    response = requests.get(f"{baseURL}{path}", headers={"Authorization": f"Bearer {access_token}"})

    try:
        return response.json()['data']
    except:
        raise Exception(f"Error:\n{response.json()}")

def queryPbxAssociatedCustomers(access_token, cloudPbxId):
    path = f"/dm/open_api/v1/cloud_pbx/instances/{cloudPbxId}/customers"

    response = requests.get(f"{baseURL}{path}", headers={"Authorization": f"Bearer {access_token}"})

    try:
        return response.json()['data']
    except:
        raise Exception(f"Error:\n{response.json()}")

def queryAvailableRegions(access_token):
    path = "/dm/open_api/v1/cluster/regions"

    response = requests.get(f"{baseURL}{path}", headers={"Authorization": f"Bearer {access_token}"})
    
    try:
        return response.json()['data']
    except:
        raise Exception(f"Error:\n{response.json()}")

def queryAvailableDomainNames(access_token, regionIds:list):
    path = f"/dm/open_api/v1/cluster/domains"

    # This may be a shit and messy way of doing this, but it lets people pass a regular python list as an argument and it works
    regionIds_formatted = ""
    for region in regionIds:
        regionIds_formatted += f"{region},"
    regionIds_formatted = regionIds_formatted[:-1]

    response = requests.get(f"{baseURL}{path}?regionIds={regionIds_formatted}", headers={"Authorization": f"Bearer {access_token}"})

    try:
        return response.json()['data']
    except:
        raise Exception(f"Error:\n{response.json()}")

def getPbxPasswordlessLoginURL(access_token, cloudPbxId):
    path = f"/dm/open_api/v1/cloud_pbx/instances/{cloudPbxId}/password_free_login_url"

    response = requests.get(f"{baseURL}{path}", headers={"Authorization": f"Bearer {access_token}"})
    
    try:
        return response.json()["data"]["passwordFreeLoginUrl"]
    except:
        raise Exception(f"Error:\n{response.json()}\nResponse data string is empty. Passwordless login may not be enabled for this PBX?")

def createPBX():
    pass

def deletePBX(access_token, cloudPbxIDs:list):
    path = "/dm/open_api/v1/cloud_pbx/instances"

    jsonContent = {
        "cloudPbxIds": cloudPbxIDs
    }

    response = requests.delete(f"{baseURL}{path}", data=jsonContent, headers={"Authorization": f"Bearer {access_token}"})

    try:
        return response.json()
    except:
        raise Exception(f"Error:\n{response.content}")

def sendPbxActivationEmails():
    pass

def startPBX(access_token, cloudPbxId):
    path = f"/dm/open_api/v1/cloud_pbx/instances/{cloudPbxId}/start"

    response = requests.put(f"{baseurl}{path}", headers={"Authorization": f"Bearer {access_token}"})


    try:
        return response.json()
    except:
        raise Exception(f"Error:\n{response.content}")

def stopPBX(access_token, cloudPbxId):
    path = f"/dm/open_api/v1/cloud_pbx/instances/{cloudPbxId}/stop"

    response = requests.put(f"{baseurl}{path}", headers={"Authorization": f"Bearer {access_token}"})


    try:
        return response.json()
    except:
        raise Exception(f"Error:\n{response.content}")

def updatePbxInfo(access_token, cloudPbxId, name, upgradeInPbx:bool, im:bool, pbxApi:bool, passwordlessLogin:bool, superiorPasswordlessLogin:bool, provisionViaTemplate:bool, trunkConfigurationAccess:bool):
    path = f"/dm/open_api/v1/cloud_pbx/instances/{cloudPbxId}"

    jsonContent = {
        "name": name,
        "upgradeInPbx": "Enabled" if upgradeInPbx == True else "Disabled",
        "im": "Enabled" if im == True else "Disabled",
        "pbxApi": "Enabled" if pbxApi == True else "Disabled",
        "passwordlessLogin": "Enabled" if passwordlessLogin == True else "Disabled",
        "allowSuperiorPasswordlessLogin": "Enabled" if superiorPasswordlessLogin == True and passwordlessLogin == True else "Disabled",
        "provisioningViaTemplate": "Enabled" if provisionViaTemplate == True else "Disabled",
        "trunkConfigurationAccess": "Enabled" if trunkConfigurationAccess == True else "Disabled"
    }

    response = requests.put(f"{baseURL}{path}", headers={"Authorization": f"Bearer {access_token}"}, data=jsonContent)

    try:
        return response.json()
    except:
        raise Exception(f"Error:\n{response.content}")

def updatePbxDIDs(access_token, cloudPbxId, didRelations):
    pass

def updatePbxCustomers(access_token, cloudPbxId, customerIds:list):
    path = f"/dm/open_api/v1/cloud_pbx/instances/{cloudPbxId}/customers"

    jsonContent = {
        "customerIds": customerIds
    }

    response = requests.put(f"{baseURL}{path}", data=jsonContent, headers={"Authorization": f"Bearer {access_token}"})

    try:
        return response.json()
    except:
        raise Exception(f"Error:\n{response.content}")

def resizePbx(access_token, cloudPbxId, extensionCapacity, concurrentCallCapacity, recordingStatus:bool, recordingCapacity, transcriptionCapacity, receptionistCapacity, transcriptionPack, receptionistPack):
    path = f"/dm/open_api/v1/cloud_pbx/instances/{cloudPbxId}/capacity"

    jsonContent = {
        "extensionCapacity": extensionCapacity,
        "concurrentCallCapacity": concurrentCallCapacity,
        "recordingStatus": "Enabled" if recordingStatus == True else "Disabled",
        "recordingCapacity": recordingCapacity,
        "transcriptionCapacity": transcriptionCapacity,
        "receptionistCapacity": receptionistCapacity,
        "transcriptionPack": transcriptionPack,
        "receptionistPack": receptionistPack
    }

    response = requests.put(f"{baseURL}{path}", data=jsonContent, headers={"Authorization": f"Bearer {access_token}"})

    try:
        return response.json()
    except:
        raise Exception(f"Error:\n{response.content}")

def resetPbxAdminPassword(access_token, cloudPbxId):
    path = f"/dm/open_api/v1/cloud_pbx/instances/{cloudPbxId}/reset_administrator_password"

    response = requests.post(f"{baseURL}{path}", headers={"Authorization": f"Bearer {access_token}"})

    try:
        return response.json()
    except:
        raise Exception(f"Error:\n{response.content}")



