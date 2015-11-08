#coding=utf8
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import views
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin,flatpages
admin.autodiscover()
admin.site.site_header = '选课管理系统'
urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'', include('xkxt.verification.urls')),
    url(r'^main/', include('xkxt.course.urls')),
    url(r"^main/$",views.main,name="main"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
)

urlpatterns += patterns('', (
    r'^static/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}
))
# urlpatterns += patterns('',
#     url(r'^captcha/', include('captcha.urls')),
# )
