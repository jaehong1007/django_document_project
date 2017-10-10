from django.contrib import admin

from model.models import User, Car, Manufacturer

admin.site.register(Car)
admin.site.register(Manufacturer)
admin.site.register(User)
