from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'email', 'listing_id','listing', 'contact_date')
    list_display_links= ('user_id', 'name')
    search_fields=('name', 'email','listing')
    list_per_page=25

admin.site.register(Contact, ContactAdmin)
