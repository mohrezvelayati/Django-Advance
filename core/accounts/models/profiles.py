from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .users import User



class Profile(models.Model):
    """ Profile class for each user wich is being created to hold the information """
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    """ This function creates a profile for a new user after saving a new user."""
    if created:
        Profile.objects.create(user=instance)