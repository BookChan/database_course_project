from django.conf.urls import patterns, include,url
import views

urlpatterns = patterns('',
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    )
