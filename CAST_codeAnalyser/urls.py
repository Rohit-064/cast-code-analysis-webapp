"""CAST_codeAnalyser URL Configuration"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from Analyser import views

router = routers.DefaultRouter()
router.register(r'api/todos', views.TodoView, 'todo')

urlpatterns = [
    url('admin/', admin.site.urls),         
    url('', include(router.urls)),
    url(r'api/code-analyser', views.code_analyser.as_view(), name='code_analyser')
]