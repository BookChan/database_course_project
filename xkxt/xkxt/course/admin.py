#coding=utf8
from django.contrib import admin

import models




@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
        list_display = ("id","name","creadit")


@admin.register(models.Section,models.Take)
class tmp2Admin(admin.ModelAdmin):
        pass
