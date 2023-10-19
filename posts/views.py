from datetime import timezone
from rest_framework import viewsets, permissions, status  # <-- Add 'status' here
from rest_framework.response import Response
from .models import Article, Magazine, Podcast, Video
from .serializers import ArticleSerializer, MagazineSerializer, PodcastSerializer, VideoSerializer
from .permissions import IsOwnerOrReadOnly  # Make sure to import your custom permission class

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            creation_date = request.data.get('creation', None)
            if creation_date:
                request.data['creation'] = creation_date
            else:
                request.data['creation'] = timezone.now()
            return super().create(request, *args, **kwargs)
        else:
            return Response({"error": "You must be authenticated to create an article"}, status=status.HTTP_403_FORBIDDEN)

class MagazineViewSet(viewsets.ModelViewSet):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            creation_date = request.data.get('creation', None)
            if creation_date:
                request.data['creation'] = creation_date
            else:
                request.data['creation'] = timezone.now()
            return super().create(request, *args, **kwargs)
        else:
            return Response({"error": "You must be authenticated to create a magazine"}, status=status.HTTP_403_FORBIDDEN)


class PodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            creation_date = request.data.get('creation', None)
            if creation_date:
                request.data['creation'] = creation_date
            else:
                request.data['creation'] = timezone.now()
            return super().create(request, *args, **kwargs)
        else:
            return Response({"error": "You must be authenticated to create a magazine"}, status=status.HTTP_403_FORBIDDEN)


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            creation_date = request.data.get('creation', None)
            if creation_date:
                request.data['creation'] = creation_date
            else:
                request.data['creation'] = timezone.now()
            return super().create(request, *args, **kwargs)
        else:
            return Response({"error": "You must be authenticated to create a magazine"}, status=status.HTTP_403_FORBIDDEN)

