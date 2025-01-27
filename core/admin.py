from django.contrib import admin
from .models import Worker
# Register your models here.

class WorkerAdmin(admin.ModelAdmin):
    list_display = ['id','name','position','branch']
