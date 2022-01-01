from django.contrib import admin
from findcafe.models import Cafe
# Register your models here.


class CafeListAdmin(admin.ModelAdmin):
    list_display = ['name', 'location',  'wifi', 'toilet', 'smokingarea', 'ac_room', 'avg_price']
    search_fields = ['name', 'location', 'wifi', 'toilet', 'smokingarea', 'ac_room', 'avg_price']
    list_per_page = 10 
admin.site.register(Cafe, CafeListAdmin)
 

