import requests


baseURL = "https://ycm.yeastar.com"


def queryAllSharedTrunks(access_token):
    path = "/dm/open_api/v1/shared_trunk"

    response = requests.get(f"{baseURL}{path}", headers={"Authorization": f"Bearer {access_token}"})

    try:
        return response.json()["data"]
    except:
        raise Exception(f"Error:\n{response.content}")

def queryAvailableSharedTrunks(access_token):
    path = "/dm/open_api/v1/shared_trunk/name/acl"

    response = requests.get(f"{baseURL}{path}", headers={"Authorization": f"Bearer {access_token}"})

    try:
        return response.json()["data"]
    except:
        raise Exception(f"Error:\n{response.content}")

def querySharedTrunk(access_token, trunkId):
    path = f"/dm/open_api/v1/shared_trunk/{trunkId}"

    response = requests.get(f"{baseURL}{path}", headers={"Authorization": f"Bearer {access_token}"})

    try:
        return response.json()["data"]
    except:
        raise Exception(f"Error:\n{response.content}")

def querySharedTrunkStatus(access_token, trunkId):
    path = f"/dm/open_api/v1/shared_trunk/{trunkId}/status"

    response = requests.get(f"{baseURL}{path}", headers={"Authorization": f"Bearer {access_token}"})

    try:
        return response.json()["data"]
    except:
        raise Exception(f"Error:\n{response.content}")

def querySharedTrunkItsp(access_token):
    path = f"/dm/open_api/v1/shared_trunk/itsp"

    response = requests.get(f"{baseURL}{path}", headers={"Authorization": f"Bearer {access_token}"})

    try:
        return response.json()["data"]
    except:
        raise Exception(f"Error:\n{response.content}")
