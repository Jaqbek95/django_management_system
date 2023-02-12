from django.contrib import admin

from .models import Project, Customer


admin.site.register(Project)
admin.site.register(Customer)