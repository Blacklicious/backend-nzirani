from django.contrib import admin
from .models import Article, Magazine, Podcast, Video

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('rubrique','title', 'author', 'date', 'location', 'status')

@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ('rubrique','title', 'author', 'date', 'location', 'status')

@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ('rubrique','title', 'author', 'date', 'location', 'status')

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('rubrique','title', 'author', 'date', 'location', 'status')
