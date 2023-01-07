from django.contrib import admin
from .models import *
# Register your models here.

class HelloWorldAdmin(admin.ModelAdmin):
    list_display = ('name','age')


admin.site.register(Person, HelloWorldAdmin)