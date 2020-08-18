from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=40, default="")
    city = models.CharField(max_length=40, default="")
    phone_number = PhoneNumberField()

    def __str__(self):
        return f"{self.user}"
