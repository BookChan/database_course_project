#coding=utf8
from django.db import models
from django.contrib.auth.models import User

from xkxt.organization.models import Major
SEX_CHOICES = (
    ('0','男'),
    ('1','女'),
)

class Student(models.Model):
    id = models.CharField(u"学生编号",primary_key=True,max_length=10)
    user = models.OneToOneField(User)
    name = models.CharField(u'姓名',null=False,max_length=16)
    sex = models.CharField(u'性别',choices = SEX_CHOICES,max_length = 1)
    birthday = models.DateField('生日')
    mj_id = models.ForeignKey(Major)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = u"student"
        verbose_name_plural = '学生'
