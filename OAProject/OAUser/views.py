#coding:utf-8
from django.shortcuts import render
import hashlib
from OAUser.models import Register
from django.template import RequestContext
from OAUser.form import UserLogin,UserRegister

# Create your views here.
def take_md5(content):
    hash = hashlib.md5() #创建加密实例
    hash.update(content.encode('utf8')) #hash 加密
    result = hash.hexdigest() # 得到加密结果
    return result

#注册
def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid(): #获取表单信息
            username = form.cleaned_data['username']
            namefilter = Register.objects.filter(username = username)
            if len(namefilter) > 0 :
                return render(request,'register.html',{'error':'用户名已经存在'})
            else:
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']
                if password1 != password2 :
                     return render(request,'register.html',{'error':'两次输入的密码不一致!'})
                else:
                    password = take_md5(password1)
                    email = form.cleaned_data['email']
                    phone_number = form.cleaned_data['phone_number']
                    #将表单写入数据库
                    user = Register.objects.create(username = username,password = password,email = email,phone_number = phone_number)
                    user.save()
                    return render(request,'register.html',{'username':username,'operation':'注册'})
    else:
        form = UserRegister()
        return render(request,'register.html',{'form':form})

#登录
def login(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid(): #获取表单信息
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password = take_md5(password)
            namefilter  = Register.objects.filter(username=username,password=password)
            if len(namefilter) > 0 :
                return render(request,'success.html',{'usernamne':username,'operation':'登录'})
            else:
                return render(request,'login.html',{'error':'该用户名不存在！'})
    else:
        form = UserLogin()
        return render(request,'login.html',{'form':form})
