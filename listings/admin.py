from django.contrib import admin

# Register your models here.
from.models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','price','list_date','realtor')
    list_display_link = ('id','title') # entry to record for editing
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title','description','address','price')
    list_per_page =25

admin.site.register(Listing, ListingAdmin)