
from django.urls import path
from . import views
from .views import UserLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', UserLoginView.as_view(), name="login"),
    path("staff/", views.staff_dashboard, name="staff_dashboard"),
    path('logout/', LogoutView.as_view(), name='logout'), #double-check
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile_detail, name='profile_detail'),
    path('profile/edit/', views.profile_edit, name='profile_edit')
]
