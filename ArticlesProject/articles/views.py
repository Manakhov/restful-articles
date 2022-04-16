from rest_framework import generics
from .serializers import ArticleDetailSerializer, ArticlesListSerializer
from .models import Article
from .permissions import IsOwnerOrReadOnly


class ArticleCreateView(generics.CreateAPIView):
    """View for article creating"""
    serializer_class = ArticleDetailSerializer


class ArticlesListView(generics.ListAPIView):
    """View for article list getting"""
    serializer_class = ArticlesListSerializer
    queryset = Article.objects.all()


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View for article getting, updating, deleting"""
    serializer_class = ArticleDetailSerializer
    queryset = Article.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
