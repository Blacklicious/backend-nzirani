from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/articles', views.ArticleViewSet)
router.register(r'api/magazines', views.MagazineViewSet)
router.register(r'api/podcasts', views.PodcastViewSet)
router.register(r'api/videos', views.VideoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
