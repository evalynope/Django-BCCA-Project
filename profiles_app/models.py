from django.db import models
from django.contrib.auth import get_user_model #used to call all built in User fields

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    city_state = models.CharField(
        max_length=50,
        blank=True)
    bio = models.CharField(
        max_length=200,
        blank=True)

    def __str__(self):
        return self.user.username

