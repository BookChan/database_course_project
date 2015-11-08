from django.contrib import admin
import models
# Register your models here.
@admin.register(models.Student)
class tmp3Admin(admin.ModelAdmin):
        pass
