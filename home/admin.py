from django.contrib import admin
from home.models import *

class homeAdmin(admin.ModelAdmin):
    list_display = ('id','by_user', 'which_call', 'name', 'email', 'phone', 'alternate_phone', 'billing_address', 'member_of_family', 'worth', 'favourable_apps')  
    list_filter = ('by_user','which_call', 'name', 'email', 'phone', 'alternate_phone', 'worth','favourable_apps')  
    search_fields = ('by_user__username','which_call', 'name', 'email', 'phone', 'alternate_phone', 'billing_address', 'member_of_family', 'worth', 'favourable_apps')  

admin.site.register(customer_detail, homeAdmin)

class noteAdmin(admin.ModelAdmin):
    list_display = ('id','by_user')
    search_fields = ('by_user__username',)

admin.site.register(notes, noteAdmin)
admin.site.register(reminders)