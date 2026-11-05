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

def querySharedTrunkConcurrentCalls(access_token, trunkId):
    path = f"/dm/open_api/v1/shared_trunk/{trunkId}/cc-info"

    response = requests.get(f"{baseURL}{path}", headers={"Authorization": f"Bearer {access_token}"})

    try:
        return response.json()["data"]
    except:
        raise Exception(f"Error:\n{response.content}")

def createSharedRegisterTrunk(access_token, name:str, enable:int, regionId:str, country:str, defaultRegistrationTime:int, transport:str, hostname:str, domain:str, port:int, username:str, password:str, authName:str, enbOutboundProxy:bool, outboundProxyServer:str, outboundProxyPort:int, codecSel:str, dtmfMode:str, dtmfFmtp:str, authErrorSipCode:str, authRegisterAttempt:int, globalRegisterRetryInterval:int, enbQualify:bool, enbSrtp:bool, enbT38Support:bool, enbInbandProgress:bool, ignore183WithoutSdp:bool, transparentTrans180Msg:bool, enbDedicate:bool, enbSipAuthCache:bool, unsetSips:bool, ignore100Responses:bool, callRestrictionType:str, callerIdFrom:str, didFrom:str, fromUserPart:str, fromDispNamePart:str, diversionUserPart:str, rpidUserPart:str, paiUserPart:str, paiUserPartUriFormat:str, ppiUserPart:str, maxPtime:str, enbPrivacyId:bool, enbUserPhone:bool, enbApiCallId:bool, enbEarlyMedia:bool, enbEarlyMediaFor183:bool, forceDodFrom:bool, enbSend302OnCfExternal:bool, enb100Rel:int, realm:str="", userAgent:str="", customSipHeaders:list=[], ppiUser:str="", paiUser:str="", rpidUser:str="", diversionUser:str="", fromUser:str="", fromDispName:str="", maxCallChans:int=0, backupHostname:str="", itsp:str="", remark:str="", registrationAttempts:int=0, type:str="register"):
    pass

def createSharedPeerTrunk(access_token):
    pass