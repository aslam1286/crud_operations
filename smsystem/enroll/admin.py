from django.contrib import admin
from enroll import models

@admin.register(models.Student)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'rollno', 'name', 'email', 'password')