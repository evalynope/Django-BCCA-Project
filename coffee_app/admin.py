from django.contrib import admin
from .models import CoffeeShop, Roast, BrewEntry
from profiles_app.models import Profile
admin.site.register(CoffeeShop)
admin.site.register(BrewEntry)
admin.site.register(Profile)

class BrewEntryInline(admin.TabularInline):
    model = BrewEntry
    extra = 0
    ordering = ["-date_created"]

class RoastAdmin(admin.ModelAdmin):
    list_display = ['name', 'origin', 'coffee_shop', 'is_seasonal', 'is_available']
    inlines = [BrewEntryInline]

admin.site.register(Roast, RoastAdmin)