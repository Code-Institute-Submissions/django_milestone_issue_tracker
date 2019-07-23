from django.db import models
from django.conf import settings

# Create your models here.
class UserProfile(models.Model):
    full_name = models.CharField(max_length=254, default='')
    author = models.OneToOneField(settings.AUTH_USER_MODEL, default='')
    phone = models.CharField(max_length=20, default='')
    address1 = models.CharField(max_length=254, default='')
    address2 = models.CharField(max_length=254, default='')
    postcode = models.CharField(max_length=20, default='')
    town = models.CharField(max_length=254, default='')
    county = models.CharField(max_length=254, default='')
    country = models.CharField(max_length=254, default='')

    def __str__(self):
        return self.full_name