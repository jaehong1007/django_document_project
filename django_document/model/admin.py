from django.contrib import admin

# from model.models import User, Car, Manufacturer
from .models import Car, User, Manufacturer


admin.site.register(Car)
admin.site.register(Manufacturer)
admin.site.register(User)
