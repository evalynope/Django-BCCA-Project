from django.db import models
from django.contrib.auth import get_user_model #used to call all built in User fields
from django.utils.safestring import mark_safe

User = get_user_model()

class Profile(models.Model):

    BREW_METHODS = [("espresso", "Espresso"),  
                ("pour_over", "Pour Over"),
                ("french_press", "French Press"), 
                ("drip", "Drip"), 
                ("aeropress", "AeroPress"), 
                ("moka_pot", "Moka Pot"), 
                ("other", "Other"), ]
    
    ROASTS = [
        ("light","Light"),
        ("medium","Medium"),
        ("dark","Dark")]
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile")
    first_last_name = models.CharField(
        max_length=100,
        blank=True)
    city_state = models.CharField(
        max_length=50,
        blank=True)
    bio = models.CharField(
        max_length=200,
        blank=True)
    fav_brew = models.CharField(
        max_length = 50,
        blank=True,
        choices=BREW_METHODS)
    roast_preference = models.CharField(
        max_length=50,
        choices=ROASTS,
        blank=True)

    def __str__(self):
        return self.user.username

