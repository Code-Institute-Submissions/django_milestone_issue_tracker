from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    full_name = models.CharField(max_length=254, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address1 = models.CharField(max_length=254, blank=True)
    address2 = models.CharField(max_length=254, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    town = models.CharField(max_length=254, blank=True)
    county = models.CharField(max_length=254, blank=True)
    country = models.CharField(max_length=254, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()