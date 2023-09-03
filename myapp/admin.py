from django.contrib import admin
from .models import place
from .models import Explore,Booking
# Register your models here.
admin.site.register(place)
admin.site.register(Explore)
admin.site.register(Booking)