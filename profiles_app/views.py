#PROFILE APP VIEWS
#PROFILE APP
#PROFILE APP
#PROFILE APP

from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.forms import ModelForm
from .forms import ProfileForm


def home(request):
    return render(request, "profiles_app/home.html")

class UserLoginView(LoginView):
    template_name = "profiles_app/login.html"

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST) #built in to create Django User accounts
        if form.is_valid:
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user) #imported for redirects
        return redirect("profile_detail")
    else:
        form = UserCreationForm()

    return render(request, 'profiles_app/signup.html', {"form": form})


@login_required
def profile_detail(request):
    return render(
        request,
        "profiles_app/profile_detail.html",
        {"profile": request.user.profile}
    )

    


@login_required
def profile_edit(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_detail')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profiles_app/profile_edit.html', {'form': form})