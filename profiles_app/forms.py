
from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_last_name', 'city_state', 'state', 'bio', 'fav_brew', 'roast_preference']
        labels = {
        'first_last_name': 'Full Name',
        'city_state': 'City',
        'state':'State',
        'bio': 'Bio',
        'fav_brew': 'Favorite Brew Method',
        'roast_preference': 'Preferred Roast',
    }
        

# profiles_app/forms.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        min_length=5,
        max_length=20,
        help_text="5–20 characters"
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data["username"]
        if not 5 <= len(username) <= 20:
            raise forms.ValidationError(
                "Username must be between 5 and 20 characters."
            )
        if username.isdigit():
            raise forms.ValidationError(
                "Username cannot be only numbers."
            )
        return username
