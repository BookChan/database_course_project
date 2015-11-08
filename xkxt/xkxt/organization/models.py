#coding=utf8
from django.db import models



class ClassRoom(models.Model):
      building = models.CharField(u"楼名",null=False,max_length=10)
      room_id = models.CharField(u"房间编号",null=False,max_length=10)
      capicity = models.IntegerField(u"座位数",null=False)
      def __unicode__(self):
          return self.building+self.room_id
      class Admin:
            list_display=('building','room_id','capicity')

      class Meta:

          db_table = u"classroom"
          verbose_name = "教室"
          verbose_name_plural = '教室'

class Department(models.Model):
    '''
    院系表
    '''
    id = models.CharField(u"院系编号",primary_key=True,max_length=10)
    name = models.CharField(u"院系名称",null=False,max_length=20)
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = u"department"
        verbose_name_plural = '院系'
    class Admin:
        pass

class Major(models.Model):
    '''
    专业表
    '''
    id = models.CharField(u"专业编号",primary_key=True,max_length=10)
    name = models.CharField(u"专业名称",null=False,max_length=20)
    dep_id = models.ForeignKey(Department,verbose_name="院系")
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = u"major"
        verbose_name_plural = u'专业'

