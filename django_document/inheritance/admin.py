from django.contrib import admin

from .models import Teacher, Student, School, Restaurant, Place

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(School)
admin.site.register(Place)
admin.site.register(Restaurant)