#CONFIG URLS
#CONFIG URLS
#CONFIG URLS
#CONFIG URLS


from django.contrib import admin
from django.urls import path, include
from coffee_app.models import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("coffee_app.urls")), #main part of site, empty URL. Might need to be fixed later
    path('profiles/', include('profiles_app.urls')),
  
]
