import re
import requests
from requests.structures import CaseInsensitiveDict
import json
import random


def checkexist(user, deviceid, device):
    url = "https://api.tv360.vn/public/v1/auth/exist-credential?msisdn={}".format(user)
    sessionid = "ANDROID_{}{}{}{}".format(
        random.randint(1000, 9999),
        random.randint(100000, 999999),
        random.randint(10000, 99999),
        random.randint(100, 999),
    )
    headers = CaseInsensitiveDict()
    headers["User-Agent"] = (
        "Dalvik/2.1.0 (Linux; U; Android 9; {} Build/PQ3B.190801.01311438)".format(
            device
        )
    )
    headers["osapptype"] = "ANDROID"
    headers["devicetype"] = "WEB_ANDROID"
    headers["lang"] = "vi"
    headers["deviceid"] = deviceid
    headers["devicedrmid"] = deviceid
    headers["deviceName"] = "samsung" + device
    headers["sessionid"] = sessionid
    headers["osappversion"] = "3.7"
    headers["freedata"] = "1"
    headers["Content-Type"] = "application/json"
    headers["Host"] = "api.tv360.vn"
    headers["Connection"] = "Keep-Alive"
    headers["Accept-Encoding"] = "gzip"

    resp = requests.get(url, headers=headers, verify=False)
    print(resp.text)
    respdata = resp.json()
    msg = respdata["message"]
    return msg


def login(user, password, device, deviceid):
    url = "https://api.tv360.vn/public/v1/auth/login"
    sessionid = "ANDROID_{}{}{}{}".format(
        random.randint(1000, 9999),
        random.randint(100000, 999999),
        random.randint(10000, 99999),
        random.randint(100, 999),
    )
    data = {
        "deviceInfo": {
            "deviceDrmId": deviceid,
            "deviceId": deviceid,
            "deviceName": "samsung " + device,
            "deviceType": "WEB_ANDROID",
            "osType": "ANDROID",
            "osVersion": "9",
            "screenSize": "900x1600",
            "selected": False,
        },
        "grantType": "PASS",
        "msisdn": user,
        "password": password,
    }
    data = json.dumps(obj=data, separators=(",", ":"))
    headers = CaseInsensitiveDict()
    headers["User-Agent"] = (
        "Dalvik/2.1.0 (Linux; U; Android 9; {} Build/PQ3B.190801.01311438)".format(
            device
        )
    )
    headers["osapptype"] = "ANDROID"
    headers["devicetype"] = "WEB_ANDROID"
    headers["lang"] = "vi"
    headers["deviceid"] = deviceid
    headers["devicedrmid"] = deviceid
    headers["deviceName"] = "samsung" + device
    headers["sessionid"] = sessionid
    headers["osappversion"] = "3.7"
    headers["freedata"] = "1"
    headers["Content-Type"] = "application/json"
    headers["Content-Length"] = str(len(data))
    headers["Host"] = "api.tv360.vn"
    headers["Connection"] = "Keep-Alive"
    headers["Accept-Encoding"] = "gzip"

    resp = requests.post(url, headers=headers, data=data, verify=False)
    respdata = resp.json()
    accesstoken = respdata["data"]["accessToken"]
    refrestoken = respdata["data"]["refreshToken"]
    return accesstoken, refrestoken


def getotp(user, device, deviceid):
    url = "https://api.tv360.vn/public/v1/auth/get-otp-login"

    sessionid = "ANDROID_{}{}{}{}".format(
        random.randint(1000, 9999),
        random.randint(100000, 999999),
        random.randint(10000, 99999),
        random.randint(100, 999),
    )
    data = {"msisdn": user}
    data = json.dumps(obj=data, separators=(",", ":"))
    headers = CaseInsensitiveDict()
    headers["User-Agent"] = (
        "Dalvik/2.1.0 (Linux; U; Android 9; {} Build/PQ3B.190801.01311438)".format(
            device
        )
    )
    headers["osapptype"] = "ANDROID"
    headers["devicetype"] = "WEB_ANDROID"
    headers["lang"] = "vi"
    headers["deviceid"] = deviceid
    headers["devicedrmid"] = deviceid
    headers["deviceName"] = "samsung" + device
    headers["sessionid"] = sessionid
    headers["osappversion"] = "3.7"
    headers["freedata"] = "1"
    headers["Content-Type"] = "application/json"
    headers["Content-Length"] = str(len(data))
    headers["Host"] = "api.tv360.vn"
    headers["Connection"] = "Keep-Alive"
    headers["Accept-Encoding"] = "gzip"

    resp = requests.post(url, headers=headers, data=data, verify=False)
    respdata = resp.json()
    msg = respdata["message"]
    return msg


def regis(user, device, otp, deviceid):
    url = "https://api.tv360.vn/public/v1/auth/login"
    sessionid = "ANDROID_{}{}{}{}".format(
        random.randint(1000, 9999),
        random.randint(100000, 999999),
        random.randint(10000, 99999),
        random.randint(100, 999),
    )
    data = {
        "deviceInfo": {
            "deviceDrmId": deviceid,
            "deviceId": deviceid,
            "deviceName": device,
            "deviceType": "WEB_ANDROID",
            "osType": "ANDROID",
            "osVersion": "9",
            "screenSize": "900x1600",
            "selected": False,
        },
        "grantType": "OTP",
        "msisdn": user,
        "otp": otp,
    }
    data = json.dumps(obj=data, separators=(",", ":"))
    headers = CaseInsensitiveDict()
    headers["User-Agent"] = (
        "Dalvik/2.1.0 (Linux; U; Android 9; {} Build/PQ3B.190801.01311438)".format(
            device
        )
    )
    headers["osapptype"] = "ANDROID"
    headers["devicetype"] = "WEB_ANDROID"
    headers["lang"] = "vi"
    headers["deviceid"] = deviceid
    headers["devicedrmid"] = deviceid
    headers["deviceName"] = "samsung" + device
    headers["sessionid"] = sessionid
    headers["osappversion"] = "3.7"
    headers["freedata"] = "1"
    headers["Content-Type"] = "application/json"
    headers["Content-Length"] = str(len(data))
    headers["Host"] = "api.tv360.vn"
    headers["Connection"] = "Keep-Alive"
    headers["Accept-Encoding"] = "gzip"

    resp = requests.post(url, headers=headers, data=data, verify=False)
    respdata = resp.json()
    accesstoken = respdata["data"]["accessToken"]
    refrestoken = respdata["data"]["refreshToken"]
    userid = respdata["data"]["userId"]
    return accesstoken, refrestoken, userid


def createPassword(accesstoken, deviceid, device):
    url = "https://api.tv360.vn/api/v1/user/create-password"
    sessionid = "ANDROID_{}{}{}{}".format(
        random.randint(1000, 9999),
        random.randint(100000, 999999),
        random.randint(10000, 99999),
        random.randint(100, 999),
    )
    data = {"confirmPassword": "qwert123", "newPassword": "qwert123"}
    data = json.dumps(obj=data, separators=(",", ":"))
    headers = CaseInsensitiveDict()
    headers["User-Agent"] = (
        "Dalvik/2.1.0 (Linux; U; Android 9; {} Build/PQ3B.190801.01311438)".format(
            device
        )
    )
    headers["osapptype"] = "ANDROID"
    headers["devicetype"] = "WEB_ANDROID"
    headers["lang"] = "vi"
    headers["deviceid"] = deviceid
    headers["devicedrmid"] = deviceid
    headers["deviceName"] = "samsung " + device
    headers["sessionid"] = sessionid
    headers["osappversion"] = "3.7"
    headers["freedata"] = "1"
    headers["Content-Type"] = "application/json; charset=UTF-8"
    headers["Content-Length"] = str(len(data))
    headers["Host"] = "api.tv360.vn"
    headers["Connection"] = "Keep-Alive"
    headers["Accept-Encoding"] = "gzip"
    headers["Authorization"] = "Bearer {}".format(accesstoken)

    resp = requests.post(url, headers=headers, data=data, verify=False)
    respdata = resp.json()
    msg = respdata["message"]
    return msg


def checkAccept(userid, device, deviceid, accesstoken):
    url = "https://api.tv360.vn/api/v1/user/check-accept-policy"
    sessionid = "ANDROID_{}{}{}{}".format(
        random.randint(1000, 9999),
        random.randint(100000, 999999),
        random.randint(10000, 99999),
        random.randint(100, 999),
    )
    data = {
        "deviceInfo": {
            "deviceDrmId": "{}".format(deviceid),
            "deviceId": "{}".format(deviceid),
            "deviceName": device,
            "deviceType": "WEB_ANDROID",
            "osType": "ANDROID",
            "osVersion": "9",
            "screenSize": "900x1600",
            "selected": False,
        },
        "userId": "{}".format(userid),
    }
    data = json.dumps(obj=data, separators=(",", ":"))
    headers = CaseInsensitiveDict()
    headers["User-Agent"] = (
        "Dalvik/2.1.0 (Linux; U; Android 9; {} Build/PQ3B.190801.01311438)".format(
            device
        )
    )
    headers["osapptype"] = "ANDROID"
    headers["devicetype"] = "WEB_ANDROID"
    headers["lang"] = "vi"
    headers["deviceid"] = deviceid
    headers["devicedrmid"] = deviceid
    headers["deviceName"] = "samsung" + device
    headers["sessionid"] = sessionid
    headers["osappversion"] = "3.7"
    headers["freedata"] = "1"
    headers["Content-Type"] = "application/json"
    headers["Content-Length"] = str(len(data))
    headers["Host"] = "api.tv360.vn"
    headers["Connection"] = "Keep-Alive"
    headers["Accept-Encoding"] = "gzip"
    headers["Authorization"] = "Bearer {}".format(accesstoken)

    resp = requests.post(url, headers=headers, data=data, verify=False)
    respdata = resp.json()
    msg = respdata["message"]
    return msg


def authorizeGame(accesstoken, device, deviceid) -> str:
    url = "http://ws.tv360.vn/api/v1/thirdParty/wii-identifier"
    headers = CaseInsensitiveDict()
    sessionid = "ANDROID_{}{}{}{}".format(
        random.randint(1000, 9999),
        random.randint(100000, 999999),
        random.randint(10000, 99999),
        random.randint(100, 999),
    )
    headers["Content-Type"] = "application/json"
    headers["User-Agent"] = (
        "Dalvik/2.1.0 (Linux; U; Android 9; {} Build/PQ3B.190801.01311438)".format(
            device
        )
    )
    headers["osapptype"] = "ANDROID"
    headers["devicetype"] = "WEB_ANDROID"
    headers["lang"] = "vi"
    headers["deviceid"] = deviceid
    headers["devicedrmid"] = deviceid
    headers["deviceName"] = "samsung" + device
    headers["s"] = (
        "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"
    )
    headers["sessionid"] = sessionid
    headers["osappversion"] = "3.7"
    headers["freedata"] = "1"
    headers["Host"] = "ws.tv360.vn"
    headers["Accept-Encoding"] = "gzip"
    headers["Connection"] = "keep-alive"
    headers["Authorization"] = "Bearer {}".format(accesstoken)
    resp = requests.get(url, headers=headers)
    respdata = resp.json()
    accesstoken = respdata["data"]["wiiToken"]
    return accesstoken


def queryturn(device, accesstoken) -> int:
    url = "https://api-game1.tv360.vn/spingame/v1/players/_me"
    sessionid = "ANDROID_{}{}{}{}".format(
        random.randint(1000, 9999),
        random.randint(100000, 999999),
        random.randint(10000, 99999),
        random.randint(100, 999),
    )
    headers = CaseInsensitiveDict()
    headers["Connection"] = "keep-alive"
    headers["User-Agent"] = (
        "Mozilla/5.0 (Linux; Android 9; {} Build/PQ3B.190801.01311438; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36".format(
            device
        )
    )
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "*/*"
    headers["Origin"] = "https://img-ali3.tv360.vn"
    headers["X-Requested-With"] = "com.viettel.tv360"
    headers["Sec-Fetch-Site"] = "same-site"
    headers["Sec-Fetch-Mode"] = "cors"
    headers["Sec-Fetch-Dest"] = "empty"
    headers["Referer"] = "https://img-ali3.tv360.vn/"
    headers["Accept-Encoding"] = "gzip, deflate"
    headers["Accept-Language"] = "vi,vi-VN;q=0.9,en-US;q=0.8,en;q=0.7"
    headers["Authorization"] = "Bearer {}".format(accesstoken)

    resp = requests.get(url, headers=headers, verify=False)
    respdata = resp.json()
    msg = respdata["spinTurn"]
    return int(msg)


def spin(device, accesstoken):
    url = "https://api-game1.tv360.vn/turngame/v1/turngame/spin"
    sessionid = "ANDROID_{}{}{}{}".format(
        random.randint(1000, 9999),
        random.randint(100000, 999999),
        random.randint(10000, 99999),
        random.randint(100, 999),
    )
    data = {"usedSpinTurn": 0}
    data = json.dumps(obj=data, separators=(",", ":"))
    headers = CaseInsensitiveDict()
    headers["Connection"] = "keep-alive"
    headers["User-Agent"] = (
        "Mozilla/5.0 (Linux; Android 9; {} Build/PQ3B.190801.01311438; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36".format(
            device
        )
    )
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "*/*"
    headers["Origin"] = "https://img-ali3.tv360.vn"
    headers["X-Requested-With"] = "com.viettel.tv360"
    headers["Sec-Fetch-Site"] = "same-site"
    headers["Sec-Fetch-Mode"] = "cors"
    headers["Sec-Fetch-Dest"] = "empty"
    headers["Referer"] = "https://img-ali3.tv360.vn/"
    headers["Accept-Encoding"] = "gzip, deflate"
    headers["Accept-Language"] = "vi,vi-VN;q=0.9,en-US;q=0.8,en;q=0.7"
    headers["Content-Length"] = str(len(data))
    headers["Authorization"] = "Bearer {}".format(accesstoken)

    resp = requests.post(url, headers=headers, data=data, verify=False)
    respdata = resp.json()
    msg = respdata["rewardName"]
    return msg
