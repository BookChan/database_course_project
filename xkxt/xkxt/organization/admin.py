from django.contrib import admin
import models
@admin.register(models.ClassRoom)
class RoomAdmin(admin.ModelAdmin):
        list_display = ("building","room_id","capicity")

@admin.register(models.Department,models.Major)
class tmpAdmin(admin.ModelAdmin):
        pass
