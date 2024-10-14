from django.contrib import admin
from .models import TaoihdDetails, TaohidReview, Store, TaohidContact
# Register your models here.
class ReviewInline(admin.TabularInline):
    model = TaohidReview
    extra = 2

class StoreInline(admin.ModelAdmin):
    list_display = ['name', 'location']
    filter_horizontal = ['taohid_details']

class ContactInline(admin.ModelAdmin):
    list_display = ['phone', 'email', 'address']
    extra = 1

class TaoihdDetailsAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]
    list_display = ['name', 'type', 'date_added']
    search_fields = ['name', 'type']
    list_filter = ['type', 'date_added']

admin.site.register(TaoihdDetails, TaoihdDetailsAdmin)
admin.site.register(TaohidReview)
admin.site.register(Store)
admin.site.register(TaohidContact)