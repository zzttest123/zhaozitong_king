from django.urls import path,include
from TestApi import views

urlpatterns = [
    path('ztlogin/',views.ztLogin,name="ztlogin"),
    path('ztregister/',views.ztRegister,name="ztregister"),
]
