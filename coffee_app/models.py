from django.db import models
from django.contrib.auth import get_user_model 
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator
from django.conf import settings
from django.db.models import Count, F, Case, When


User = get_user_model()


class CoffeeShop(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Roast(models.Model):
    ROASTS = [
        ("light","Light"),
        ("medium","Medium"),
        ("dark","Dark")]
    
    CROWD = [("crowd-pleaser","Crowd-pleaser"),
             ("coffee enthusiast","Coffee Enthusiast")
    ]
    coffee_shop = models.ForeignKey(
        CoffeeShop,
        on_delete=models.CASCADE,
        related_name="roasts"
    )
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    tasting_notes = models.TextField()
    profile = models.CharField(
        max_length=10,
        choices=ROASTS,
        default="medium")
    crowd = models.CharField(
        max_length=20,
        choices=CROWD,
        default="coffee enthusiast")
    is_seasonal = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    is_good_to_gift = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name
    
    def most_common_brew_method(self, min_count=5):
        most_common = (
            self.brew_entries 
            .values("brew_method")
            .annotate(count=Count("id"))
            .filter(count__gte=min_count)
            .order_by("-count")
            .first()
        )
        if most_common:
            return dict(BrewEntry.BREW_METHODS).get(most_common["brew_method"])
        return None

class BrewEntry(models.Model):

    BREW_METHODS = [("espresso", "Espresso"),  
                    ("pour_over", "Pour Over"),
                    ("french_press", "French Press"), 
                    ("drip", "Drip"), 
                    ("aeropress", "AeroPress"), 
                    ("moka_pot", "Moka Pot"), 
                    ("other", "Other"), ]
    

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
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
    entry = models.TextField(
        validators=[
            MinLengthValidator(10),
            MaxLengthValidator(1000),
        ],
        help_text="20–1000 characters"
    ) 
    rating = models.PositiveSmallIntegerField(
        choices=[(i, i) for i in range(1, 6)],
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True,
        blank=True
        )
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_created"]
 

    def __str__(self):
        return f"{self.title} - {self.user.username}"



    










    
 


