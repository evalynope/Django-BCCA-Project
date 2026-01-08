from django.contrib import admin
from django.contrib import admin
from .models import Profile
from .forms import ProfileForm



class ProfileAdmin(admin.ModelAdmin):
    form = ProfileForm  # use your updated form

    # Optional: list of fields to display in the admin change list
    list_display = ("user", "first_last_name", "city_state", "fav_brew", "roast_preference")

    # Fields to show when editing a Profile in the admin
    fields = ("user", "first_last_name", "city_state", "bio", "fav_brew", "roast_preference")

# admin.site.register(Profile, ProfileAdmin)
