from django.contrib import admin
from .models import Subject, Course, Module

admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Module)
# admin.site.register(Content)