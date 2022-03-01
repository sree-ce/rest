from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserDetails(AbstractUser):
    date_of_birth = models.DateField(null=True)
    mobile_number = models.IntegerField(null=True)
    profile_picture = models.ImageField()