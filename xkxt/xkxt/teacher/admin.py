from django.contrib import admin

import  models
# Register your models here.
@admin.register(models.Teacher)
class tmp3Admin(admin.ModelAdmin):
        pass
