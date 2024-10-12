# accounts/models.py

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    phone_verified = models.BooleanField(default=False)
    # Add additional fields as needed (e.g., profile_picture, interests)

    def __str__(self):
        return self.user.username
