from django.contrib import admin

from .models import Bill, House

admin.site.register(Bill)
admin.site.register(House)