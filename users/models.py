from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    followings = models.ManyToManyField("self", related_name = "followers", symmetrical=False)
    image = models.ImageField(upload_to="profile_img/", null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()