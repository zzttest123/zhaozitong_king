from django.db import models

# Create your models here.
class zt_Register(models.Model):
    register_status = {
        (0,'成功'),
        (1,'失败'),
        (2,'未知')
    }
    username = models.CharField(max_length = 32,unique = True ,verbose_name = '用户名')
    password = models.CharField(max_length = 32,verbose_name = '密码')
    email = models.EmailField(verbose_name = '注册邮箱',null=True)
    phone_number = models.CharField(max_length = 14,unique = True,verbose_name = '电话号码')
    zt_register_status = models.IntegerField(choices=register_status,verbose_name = '注册状态')
    created_time = models.DateTimeField(auto_now_add = True,editable=False,verbose_name = '创建时间')
