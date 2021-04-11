#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from datetime import  datetime
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from TestApi.models import zt_Register
# Create your views here.

#出参：res = {"Status":"","RSTCode":"","RSTMsg":"","SendNo":"","BizType":""}
# 登录成功 0000 登录失败 0001 ，用户名不存在 0003，账号密码错误 0004，未知 0005,入参为空 0006，必填项为空 0007，
#入参：{"BizType":"","ztpin":"","ztpassword":""}


@csrf_exempt
def ztLogin(request):
    try:
        res = {"Status":"0","RSTCode":"","RSTMsg":"","BizType":"","BizTypeMsg":"登录","date":datetime.now()}
        if request.method == 'POST':
            print("入参为：{}".format(request.body))
            #判断请求body是否为空
            if request.body.decode() == '':
                res['RSTCode'] = "0006"
                res['RSTMsg'] =  "入参为空"
                #return JsonResponse(res,json_dumps_params={'ensure_ascii':False})
            else:
                #不为空，将json转化为字典
                request_str = request.body
                request_login_dict = json.loads(request_str)
            #确保字段不为空
            if request_login_dict['BizType'] == '' or request_login_dict['ztpin'] == '' or request_login_dict['ztpassword'] == '' or request_login_dict['BizType'] != '0':
                res['RSTCode'] = "0007"
                res['RSTMsg'] =  "必填项为空"
                #return JsonResponse(res,json_dumps_params={'ensure_ascii':False})
            else:
                username = request_login_dict['ztpin']
                password = request_login_dict['ztpassword']
                namefilter  = zt_Register.objects.filter(username=username,password=password)
                res['BizType'] =  request_login_dict['BizType']
                if len(namefilter) > 0 :
                    res['RSTCode'] = "0000"
                    res['RSTMsg'] =  "登录成功"
                    res['BizType'] =  "0"
                else:
                    res['RSTCode'] = "0001"
                    res['RSTMsg'] =  "用户名不存在或密码错误"
        else:
            res['Status'] = "0"
            res['RSTCode'] = "9999"
            res['RSTMsg'] = "接口请求方法不是POST！"
        return JsonResponse(res,json_dumps_params={'ensure_ascii':False})
    except Exception as e:
        res = {"Status":"Error","msg":"接口调用异常"}
        print(e)
        return JsonResponse(res,json_dumps_params={'ensure_ascii':False})




#出参：res = {"Status":"","RSTCode":"","RSTMsg":"","SendNo":"","BizType":""}
# 注册成功 0000 ， ，注册失败  0001   ， 规则错误  0003， 两次密码不匹配  0004， 参数错误  0005,  用户已存在 0006， 必填项为空 0007，
#入参：{"BizType":"","ztpin":"","ztpassword1":"","ztpassword2":"","phone_number":"","email":""}
@csrf_exempt
def ztRegister(request):
    try:
        res = {"Status":"0","RSTCode":"","RSTMsg":"","BizType":"","BizTypeMsg":"注册","date":datetime.now()}
        if request.method == 'POST':
            print("入参为：{}".format(request.body))
            #判断请求body是否为空
            if request.body.decode() == '':
                res['RSTCode'] = "0005"
                res['RSTMsg'] =  "参数错误"
            else:
                #不为空，将json转化为字典
                request_str = request.body
                request_regist_dict = json.loads(request_str)
                print("入参为：{}".format(request_regist_dict))
            #确保字段不为空
                if request_regist_dict['BizType'] == '' or request_regist_dict['ztpin'] == '' or request_regist_dict['ztpassword1'] == '' or request_regist_dict['ztpassword2'] == '' or request_regist_dict['phone_number'] == '' or request_regist_dict['BizType'] != '1':
                    res['RSTCode'] = "0007"
                    res['RSTMsg'] =  "必填项为空"
                else:
                    username = request_regist_dict['ztpin']
                    password1 = request_regist_dict['ztpassword1']
                    password2 = request_regist_dict['ztpassword2']
                    phone_number = request_regist_dict['phone_number']
                    email = request_regist_dict['email']
                    if password1 == password2 :
                        namefilter = zt_Register.objects.filter(username = username ) | zt_Register.objects.filter( phone_number = phone_number )
                        if len(namefilter) > 0:
                            res['RSTCode'] = "0006"
                            res['RSTMsg'] =  "用户名或者手机号已注册"
                            res['BizType'] =  "1"
                        else:
                            status = 0
                            zt_Register.objects.create(username = username , password = password1,phone_number=phone_number,email = email , zt_register_status = status)
                            res['RSTCode'] = "0000"
                            res['RSTMsg'] =  "注册成功"
                            res['BizType'] =  "1"
                    else:
                        res['RSTCode'] = "0004"
                        res['RSTMsg'] =  "两次密码不一致"
                        res['BizType'] =  "1"
        else:
            res['Status'] = "0"
            res['RSTCode'] = "9999"
            res['RSTMsg'] = "接口请求方法不是POST！"
        return JsonResponse(res,json_dumps_params={'ensure_ascii':False})
    except Exception as f:
        print(f)
        res = {"Status":"Error","msg":"接口调用异常"}
        return JsonResponse(res,json_dumps_params={'ensure_ascii':False})
