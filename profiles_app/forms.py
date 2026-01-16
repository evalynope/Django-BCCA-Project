
from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.password_validation import validate_password


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

    password1 = forms.CharField(
        required=True,
        label="Passwo",
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter pass'}),
    )

    password2= forms.CharField(
        required=True,
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Conformation password'}),
    )

    class Meta:
        model = User
        fields = ['email']#("username", "password1", "password2")

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

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        try:
            # Run Django's built-in password validators
            validate_password(password, self.instance)
        except forms.ValidationError as e:
            raise forms.ValidationError(e.messages)
        return password