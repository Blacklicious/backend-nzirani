from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class CommonFields(models.Model):
    rubrique = models.CharField(max_length=150, blank=True)
    title = models.CharField(max_length=500)
    content = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True, verbose_name="YouTube Video Link")
    author = models.ForeignKey(User, related_name='%(class)s_s', on_delete=models.CASCADE)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    creation = models.DateField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('archive', 'Archive')
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='inactive')

    class Meta:
        abstract = True

class Article(CommonFields):
    file = models.ImageField(upload_to='images/publications/articles/')

class Magazine(CommonFields):
    thumbnail = models.ImageField(upload_to='pdf/publications/magazines/thumbnails/')
    file = models.FileField(upload_to='pdf/publications/magazines/', null=True, blank=True)

class Podcast(CommonFields):
    thumbnail = models.ImageField(upload_to='audio/publications/podcasts/thumbnails/')
    file = models.FileField(upload_to='audio/publications/podcasts/', null=True, blank=True)

class Video(CommonFields):
    thumbnail = models.ImageField(upload_to='video/publications/videos/thumbnails/')
    file = models.FileField(upload_to='video/publications/videos/', null=True, blank=True)
