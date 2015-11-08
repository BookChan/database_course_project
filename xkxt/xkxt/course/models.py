#coding=utf8
from django.db import models
from django.contrib.auth.models import User
from xkxt.organization.models import *
from xkxt.teacher.models import *
from xkxt.student.models import *
class Course(models.Model):
    id = models.CharField(u"课程编号",primary_key=True,max_length=10)
    name = models.CharField(u'课程名称',null=False,max_length=16)
    creadit = models.IntegerField(u"学分",null=False)
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = u"course"
        verbose_name_plural = '课程'



class Section(models.Model):
    course_id = models.ForeignKey(Course)
    teachers = models.ForeignKey(Teacher)
    building = models.ForeignKey(ClassRoom)
    sec_id = models.CharField(u"学期编号",max_length=10)
    desc = models.TextField(u"课程描述")
    start_week = models.IntegerField(u"起始周",null=False)
    end_week = models.IntegerField(u"结束周",null=False)
    day = models.IntegerField(u"周几")
    start_time =   models.IntegerField(u"上课时间")
    end_time =   models.IntegerField(u"下课时间")
    MAX_NUM = models.IntegerField(u"人数",null=False)
    year = models.IntegerField(u"学年")

    def __unicode__(self):
        return self.course_id.name

    class Meta:
        db_table = u"section"
        verbose_name_plural = '开课'

class Take(models.Model):
    sec_id = models.ForeignKey(Section)
    s_id = models.ForeignKey(Student)
    score = models.FloatField(u"分数")
    class Meta:
        db_table = u"take"
        verbose_name_plural = '选课'
