from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(label = '注册用户名' , max_length = 100)
    password1 = forms.CharField(label = '设置密码' , widget=forms.PasswordInput())
    password2 = forms.CharField(label = '确认密码' , widget=forms.PasswordInput())
    email = forms.EmailField(label = '电子邮件')
    phone_number = forms.CharField(label = '手机号码' , max_length = 15)

class UserLogin(forms.Form):
    username = forms.CharField(label = '用户名',max_length = 100)
    password = forms.CharField(label = '密码',widget = forms.PasswordInput())
