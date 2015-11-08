#coding=utf8
from django.conf.urls import patterns, include,url
import views

urlpatterns = patterns('',
    url(r'^course_query/$', views.course_query, name='course_query'),
     url(r'^mycourse/$', views.mycourse, name='mycourse'),
     url(r'^mygrade/$', views.mygrade, name='mygrade'),url(r'^mygrade/$', views.mygrade, name='mygrade'),
     url(r'^course.html', views.show_course, name='showcourse'),

    )
