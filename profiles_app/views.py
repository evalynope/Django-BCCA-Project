#PROFILE APP VIEWS
#PROFILE APP
#PROFILE APP
#PROFILE APP


from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Profile
from django.forms import ModelForm
from .forms import ProfileForm
from django.urls import reverse_lazy


def home(request):
    return render(request, "profiles_app/home.html")

class UserLoginView(LoginView):
    template_name = "profiles_app/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        user = self.request.user
        if user.is_staff:
            return reverse_lazy("staff_dashboard")
        return "/"
    
def staff_check(user):
    return user.is_staff

@user_passes_test(staff_check)
def staff_dashboard(request):
    return render(request, "profiles_app/staff_dashboard.html")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(
                user=user,
                first_last_name='',
                city_state='',
                bio='',
                fav_brew='',
                roast_preference='',
            )
            login(request, user) 
            return redirect("profile_detail") #double-check
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





