from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name=models.CharField(max_length=12, blank=True)
    middle_name= models.CharField(max_length=12, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    city= models.CharField(max_length=12, blank=True)
    district= models.CharField(max_length=12, blank=True)
    state= models.CharField(max_length=12, blank=True)
    address = models.TextField(max_length=500, blank=True)
    pancard= models.CharField(max_length=12, blank=True)
    pincode= models.CharField(max_length=12, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(default='default-avatar.png', upload_to='users/', null=True, blank=True)
    adhar_image1 = models.ImageField(upload_to='users/', null=True, blank=True)
    adhar_image2 = models.ImageField(upload_to='users/', null=True, blank=True)
    pancard_image = models.ImageField(upload_to='users/', null=True, blank=True)
    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()