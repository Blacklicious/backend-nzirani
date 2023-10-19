from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='contact')
    telephone = models.CharField(max_length=15, null=True, blank=True)
    adresse = models.CharField(max_length=100, null=True, blank=True)
    business = models.CharField(max_length=50, null=True, blank=True)
    job = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Contact.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.contact.save()

class RawContact(models.Model):
    category = models.CharField(max_length=50, null=True, blank=True) # name - email - phone - number - website
    platform = models.CharField(max_length=50, null=True, blank=True) # mali gov - google - facebook - orange mali - moov
    value = models.CharField(max_length=100, null=True, blank=True) # ouwei@niow.vef - huivviue - 213112  
    note = models.CharField(max_length=150, null=True, blank=True) # verified
    status = models.CharField(max_length=50, null=True, blank=True) # verified

    def __str__(self):
        return self.value
    
class Lead(models.Model):
    category = models.CharField(max_length=50, null=True, blank=True) # personnel(contact) - professionel (business+contact) 
    origin = models.CharField(max_length=100, null=True, blank=True) # Tmak Corporation+info
    name = models.CharField(max_length=100, null=True, blank=True) # salimata traore
    email = models.CharField(max_length=100, null=True, blank=True) # salimata@barrick.com
    phone = models.CharField(max_length=20, null=True, blank=True) # (+223)74732332
    business = models.CharField(max_length=100, null=True, blank=True) # Barrick
    job = models.CharField(max_length=100, null=True, blank=True) # sale assosiate
    subject = models.CharField(max_length=100, null=True, blank=True) # event cover by T-MAK corp
    message = models.TextField( null=True, blank=True) 
    location = models.CharField(max_length=100, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, default='awaiting', blank=True)

    def __str__(self):
        return self.time.strftime('%Y-%m-%d %H:%M:%S')
