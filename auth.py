import requests


baseURL = "https://ycm.yeastar.com"


def getAccessToken(clientID:str, clientSecret:str, userAgent="PySDK"):
    authorizationPath = "/dm/open_api/oauth/token"
    grant_type = "client_credentials"

    jsonContent = {
        'grant_type': grant_type,
        'client_id': clientID,
        'client_secret': clientSecret,
    }

    headersContent = {'User-Agent': userAgent}


    response = requests.post(f"{baseURL}{authorizationPath}", data=jsonContent, headers=headersContent)
    accessToken = response.json()['access_token']
    refreshToken = response.json()['refresh_token']
    tokenType = response.json()['token_type']
    expiresIn = response.json()['expires_in']
    jti = response.json()['jti']
    
    return accessToken, refreshToken, tokenType, expiresIn, jti

def refreshAccessToken(refresh_token):
    refreshTokenPath = "/dm/open_api/oauth/token"
    grant_type = "refresh_token"

    jsonContent = {
        'grant_type': grant_type,
        'refresh_token': refresh_token
    }

    response = requests.post(f"{baseURL}{refreshTokenPath}", data=jsonContent)

