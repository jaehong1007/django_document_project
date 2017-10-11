from django.contrib import admin

# from model.models import User, Car, Manufacturer
from .models import (
    Car,
    User,
    Manufacturer,
    Topping,
    Pizza,
    FacebookUser,
    InstagramUser,
    Membership, Group, Idol,
    Place, Restaurant, Waiter
    )

admin.site.register(Car)
admin.site.register(Manufacturer)
admin.site.register(User)
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(FacebookUser)
admin.site.register(InstagramUser)
admin.site.register(Idol)
admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Waiter)