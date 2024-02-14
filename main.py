import random
from function import *

deviceid = "DRM_A_TV360_{}c{}e{}bc{}ca{}".format(
    random.randint(10, 99),
    random.randint(10, 99),
    random.randint(10, 99),
    random.randint(10, 99),
    random.randint(10, 99),
)
device = "SM-G977N"
# dangky--------------
phone = "0865933692"
msg = checkexist(phone, deviceid, device)
print(msg)
msg = getotp(phone, device, deviceid)
print(msg)
otp = input("otp: ")
accesstoken, refrestoken, userid = regis(
    user=phone, device=device, otp=otp, deviceid=deviceid
)
msg = createPassword(accesstoken=accesstoken, deviceid=deviceid, device=device)
msg = checkAccept(
    userid=userid, device=device, deviceid=deviceid, accesstoken=accesstoken
)
print(msg)

#login 
#accesstoken, refrestoken = login(phone, "qwert123", device, deviceid)

Từ lần sau thì chỉ cần loging là đc
#quay
# tokengame = authorizeGame(accesstoken=accesstoken, device=device, deviceid=deviceid)
# turn = queryturn(device=device, accesstoken=tokengame)
#trả về số lượng lượt quay
#còn cái trả lời câu hỏi tôi chưa làm.
# print(turn)
# reward = spin(device=device, accesstoken=tokengame)
# print(reward)
