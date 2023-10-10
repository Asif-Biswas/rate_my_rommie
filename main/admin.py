from django.contrib import admin
from .models import Roommate, Address, RoommateRating, AddressRating

# Register your models here.
admin.site.register(Roommate)
admin.site.register(Address)

class RoommateRatingAdmin(admin.ModelAdmin):
    list_display = ('roommate', 'attribute', 'rating', 'is_default')
    list_filter = ('roommate', 'attribute', 'rating', 'is_default')
    search_fields = ('roommate', 'attribute', 'rating', 'is_default')

admin.site.register(RoommateRating, RoommateRatingAdmin)

class AddressRatingAdmin(admin.ModelAdmin):
    list_display = ('address', 'attribute', 'rating', 'is_default')
    list_filter = ('address', 'attribute', 'rating', 'is_default')
    search_fields = ('address', 'attribute', 'rating', 'is_default')

admin.site.register(AddressRating, AddressRatingAdmin)