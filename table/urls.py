"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path(r'', views.table, name='table'),
    path(r'setting/', views.setting, name='setting'),
    path(r'login/',views.login),
    path(r'login/g/callback',views.g_callback),
    path(r'timetables/create',views.createTimetable),
    path(r'api/v1/schedules/json',views.getTableData),
    path(r'api/v1/setting/notify',views.initialize_alert),
    path(r'api/v1/notify/send',views.checkAlermStatus),
    path(r'setting/apply',views.user_settings,name='user_setting_apply')
]