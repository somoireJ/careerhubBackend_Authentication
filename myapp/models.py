from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    is_applicant = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)
    # is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Applicant(models.Model):
    user = models.OneToOneField(User, related_name="applicant", on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, null=True, blank=True)
    skills = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    portfolio = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Employer(models.Model):
    user = models.OneToOneField(User, related_name="Employer", on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username


# class Admin(models.Model):
#     user = models.OneToOneField(User, related_name="admin", on_delete=models.CASCADE)
#     # Add any additional fields specific to admin


#     def __str__(self):
#         return self.user.username
