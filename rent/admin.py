from django.contrib import admin
from rent.models import Account, House

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ['username', 'status']
    search_fields = ['username']

class HouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'location']
    search_fields = ['name']

admin.site.register(Account, AccountAdmin)
admin.site.register(House, HouseAdmin)