from django.db import models
from django.contrib.auth.models import User


from django.contrib.auth.models import User
User._meta.get_field('email')._unique = True

class PasswordReset(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid_id = models.CharField(max_length=100, null=True, blank=True)
    first_reset = models.DateTimeField(auto_now_add=True)
    last_reset = models.DateTimeField(auto_now=True)