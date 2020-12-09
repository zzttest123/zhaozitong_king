#conding:utf-8
import requests
#禅道地址
host = "http://127.0.0.1"
def login(s,username,pwd):
    url = host+"/zentao/user-login.html"
    h = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.55",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Accept-Encoding":"gzip, deflate, br",
        "Content-Type":"application/x-www-form-urlencoded",
        #"Cookie":"lang=zh-cn; theme=default; windowWidth=1536; windowHeight=754; sid=3khs5k8q2ricpt808na7qmkbh0",
        "Connection": "keep-alive",
        "Referer":host+"/zentao/user-login.html",
    }
    body1 = {
        "account":username,
        "password":pwd,
        "keepLogin[]": "on",
        "referer": host + "/zentao/my/"
    }

    #s = requests.session() 不要把session写死

    r1 =s.post(url,data= body1,headers = h)
    res = r1.content.decode("utf-8")

    return res

def is_login_sucess(res):
    if "登录失败，请检查您的用户名或密码是否填写正确。" in res:
        return False
    elif "parent.location=" in res:
        return True
    else:
        return  False

if __name__ == "__main__":
    s = requests.session()
    a = login(s,"admin","123456")
    result = is_login_sucess(a)
    print("测试结果：%s"%result)