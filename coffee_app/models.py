from django.db import models
from django.contrib.auth import get_user_model #used to call all built in User fields
from django.core.validators import MinValueValidator, MaxValueValidator #used in BrewEntry/ - rating 
from django.conf import settings

User = get_user_model()


class CoffeeShop(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Roast(models.Model):
    coffee_shop = models.ForeignKey(
        CoffeeShop,
        on_delete=models.CASCADE,
        related_name="roasts"
    )
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    tasting_notes = models.TextField()
    is_seasonal = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class BrewEntry(models.Model):

    BREW_METHODS = [("espresso", "Espresso"),  #added to avoid ambiguity. leaves 'other' option open.
                    ("pour_over", "Pour Over"),
                    ("french_press", "French Press"), 
                    ("drip", "Drip"), 
                    ("aeropress", "AeroPress"), 
                    ("moka_pot", "Moka Pot"), 
                    ("other", "Other"), ]
    

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, #will work with any relationship now
        on_delete=models.CASCADE,
        related_name="brew_entries"
    )
    roast = models.ForeignKey(
        Roast,
        on_delete=models.CASCADE,
        related_name="brew_entries"
    )
    title = models.CharField( 
        max_length=100,
        help_text="Give your brew a short descriptive title"
        )
    brew_method = models.CharField(
        max_length=50,
        choices=BREW_METHODS, #choices 
        help_text="How did you brew this roast?"
        )
    other_brew_method = models.CharField( 
        max_length=50,
        blank=True, 
        help_text="If 'Other', specify the brew method"
        )
    entry = models.TextField() #notes on experience
    rating = models.PositiveSmallIntegerField(
        choices=[(i, i) for i in range(1, 6)],
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True,
        blank=True
        )
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_created"] #orders from newest rather than oldest
 

    def __str__(self):
        return f"{self.title} - {self.user.username}"



    










    
 


