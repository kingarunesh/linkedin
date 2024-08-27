from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from dashboard.models import Profile



#NOTE :     post_save
@receiver(post_save, sender=User)
def after_save(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)