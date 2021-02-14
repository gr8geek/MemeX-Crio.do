from django.contrib import admin
from django.db.models.fields import AutoField
from .models import MyModel
# Register your models here.
class MyModeAdmin(admin.ModelAdmin):
    pass
admin.site.register(MyModel,MyModeAdmin)

