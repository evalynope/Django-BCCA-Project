
from django.forms import ModelForm
from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_last_name', 'city_state', 'state', 'bio', 'fav_brew', 'roast_preference']
        labels = {
        'first_last_name': 'Full Name',
        'city_state': 'City & State',
        'state':'State,'
        'bio' 'Biography',
        'fav_brew': 'Favorite Brew Method',
        'roast_preference': 'Preferred Roast',
    }