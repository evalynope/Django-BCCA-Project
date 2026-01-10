#CONFIG URLS
#CONFIG URLS
#CONFIG URLS
#CONFIG URLS


from django.contrib import admin
from django.urls import path, include
from coffee_app.models import *
from profiles_app import views as profiles_views
from django.conf.urls.static import static



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("coffee_app.urls")), #main part of site
    path('profiles/', include('profiles_app.urls')),
  
]

