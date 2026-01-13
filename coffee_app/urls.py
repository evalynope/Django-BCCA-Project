#/coffee_app/urls.py 
#COFFEE
#COFFEE
#COFFEE


from django.urls import path
from . import views

urlpatterns = [
    path('', views.roast_list, name="roast_list"), #works with /roasts/ ?
    path("<int:pk>/", views.roast_details, name="roast_details"),
    path("brews/new/", views.brewentry_create, name="brewentry_create"),
    path("brews/", views.brewentry_list, name="brewentry_list"),
    path("brews/<int:pk>/", views.brewentry_detail, name="brewentry_detail"),
    path("brews/<int:pk>/edit/", views.brewentry_update, name="brewentry_update"),
    path("brews/<int:pk>/delete/", views.brewentry_delete, name="brewentry_delete"),
    path("brews/community/", views.community, name ="community"),
    path("roasts/new/", views.roast_create, name="roast_create"),
    path("roasts/<int:pk>/edit/", views.roast_update, name="roast_update"),
    path("roasts/<int:pk>/delete/", views.roast_delete, name="roast_delete")
]



