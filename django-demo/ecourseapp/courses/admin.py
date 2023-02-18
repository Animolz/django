from django.contrib import admin
from .models import *

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'createdDate', 'active']
    list_filter = ['subject', 'createdDate']
    search_fields = ['id', 'subject']


# Register your models here.
admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
