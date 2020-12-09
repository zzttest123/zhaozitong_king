#coding=utf-8
import requests
import json
url = "http://localhost:5555/discuz/upload/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1"
h = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded"
}
d = {
    "fastloginfield":"username",
    "username":"admin",
    "password":"123456",
    "quickforward":"yes",
    "handlekey":"ls"
}

s = requests.session()
r = s.post(url,data=d,headers = h,verify = False)
print(r.text)
print(r.status_code)

body = {
    "formhash":"a9417279",
    "posttime":"1607443861",
    "wysiwyg":1,
    "subject":"cehs111i",
    "message":"hhahaahhahhahahhaaaaaaaaaaaaaaaaaaaaaa",
    "replycredit_extcredits":0,
    "replycredit_times":1,
    "replycredit_membertimes":1,
    "replycredit_random":100,
    "usesig":1,
    "allownoticeauthor":1
}
url2 = "http://localhost:5555/discuz/upload/forum.php?mod=post&action=newthread&fid=2&extra=&topicsubmit=yes"
r2 = s.post(url2,data=body,headers = h)
print(r2.status_code)
print(r2.text)
