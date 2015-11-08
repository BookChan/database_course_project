#coding=utf8
from django import template
import re
register = template.Library()
trans2cn = {"Auth":u"认证授权","Sites":u"站点","Xkxt":u"选课系统",
"Student":u"学生","Teacher":u"老师",u"Organization":u"组织机构","Course":"课程",
"Flat":u"通知管理"}


def app2cn(appname):
    appname = unicode(appname)
    for k,v in trans2cn.iteritems():
        if re.match(k,appname):
            return v
    return appname

@register.filter(name='transto')
def transto(value):
    if not isinstance(value,unicode):
        value = unicode(value)
    return  app2cn(value)
