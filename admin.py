from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import SafeZone, Alert, Report

admin.site.register(SafeZone)
admin.site.register(Alert)
admin.site.register(Report)