from django.db import models
from django.contrib.auth import get_user_model #used to call all built in User fields


User = get_user_model()

class Profile(models.Model):
    US_STATES = [
    ("AL", "Alabama"),
    ("AK", "Alaska"),
    ("AZ", "Arizona"),
    ("AR", "Arkansas"),
    ("CA", "California"),
    ("CO", "Colorado"),
    ("CT", "Connecticut"),
    ("DE", "Delaware"),
    ("FL", "Florida"),
    ("GA", "Georgia"),
    ("HI", "Hawaii"),
    ("ID", "Idaho"),
    ("IL", "Illinois"),
    ("IN", "Indiana"),
    ("IA", "Iowa"),
    ("KS", "Kansas"),
    ("KY", "Kentucky"),
    ("LA", "Louisiana"),
    ("ME", "Maine"),
    ("MD", "Maryland"),
    ("MA", "Massachusetts"),
    ("MI", "Michigan"),
    ("MN", "Minnesota"),
    ("MS", "Mississippi"),
    ("MO", "Missouri"),
    ("MT", "Montana"),
    ("NE", "Nebraska"),
    ("NV", "Nevada"),
    ("NH", "New Hampshire"),
    ("NJ", "New Jersey"),
    ("NM", "New Mexico"),
    ("NY", "New York"),
    ("NC", "North Carolina"),
    ("ND", "North Dakota"),
    ("OH", "Ohio"),
    ("OK", "Oklahoma"),
    ("OR", "Oregon"),
    ("PA", "Pennsylvania"),
    ("RI", "Rhode Island"),
    ("SC", "South Carolina"),
    ("SD", "South Dakota"),
    ("TN", "Tennessee"),
    ("TX", "Texas"),
    ("UT", "Utah"),
    ("VT", "Vermont"),
    ("VA", "Virginia"),
    ("WA", "Washington"),
    ("WV", "West Virginia"),
    ("WI", "Wisconsin"),
    ("WY", "Wyoming"),
]


    BREW_METHODS = [("Espresso", "Espresso"),  
                ("Pour Over", "Pour Over"),
                ("French press", "French Press"), 
                ("Drip", "Drip"), 
                ("AeroPress", "AeroPress"), 
                ("Moka Pot", "Moka Pot"), 
                ("Other", "Other"), ]
    
    ROASTS = [
        ("light","Light"),
        ("medium","Medium"),
        ("dark","Dark")]
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile")
    first_last_name = models.CharField(
        max_length=40,
        blank=True)
    city_state = models.CharField(
        max_length=50,
        blank=True)
    state = models.CharField(
        max_length=2,
        choices=US_STATES,
        blank=True,
        null=True)
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

