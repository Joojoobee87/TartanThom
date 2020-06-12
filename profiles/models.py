from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserProfile(models.Model):
    """ Provide Users with order history details and account information """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile_user")

    def __str__(self):
        return self.user