from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    full_name = models.CharField(max_length=254, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, default='')
    address1 = models.CharField(max_length=254, default='')
    address2 = models.CharField(max_length=254, default='')
    postcode = models.CharField(max_length=20, default='')
    town = models.CharField(max_length=254, default='')
    county = models.CharField(max_length=254, default='')
    country = models.CharField(max_length=254, default='')

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()