# coding:utf-8
import  requests

r = requests.get("http://localhost:5555/iwebshop/")
print(r.status_code)
#print(r.text)

b = requests.get("https://www.baidu.com/")
print(b.url)
print(b.encoding)
print(b.content)
print(b.headers)
print(b.cookies)
print(b.text)
print(b.raw)
b.encoding = 'utf-8'
print(b.text)

