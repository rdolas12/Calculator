from django.contrib import admin

# Register your models here.
from .models import Calculate
class CalculateAdmin(admin.ModelAdmin):
    list_display = ['num1','num2','output']

admin.site.register(Calculate,CalculateAdmin)