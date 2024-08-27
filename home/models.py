from django.db import models

from django.contrib.auth.models import User


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=2000)
    created_date = models.DateField(auto_now_add=True)
    review = models.BooleanField(default=False)