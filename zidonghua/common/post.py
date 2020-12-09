# coding:utf-8
import requests
import json
#help(requests)
ceshi  = {'zzt' : '111','zzy' :'112'}
data_json = json.dumps(ceshi)
r = requests.post('https://httpbin.org/post', json=data_json)
print(data_json)
print(r.status_code)
print(r.text)
