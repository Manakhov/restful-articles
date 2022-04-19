from rest_framework import generics
from .serializers import ArticleSerializer
from .models import Article
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly


class ArticleListCreateView(generics.ListCreateAPIView):
    """View for article list getting or article creating"""
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = (IsAdminOrReadOnly, )


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View for article getting, updating, deleting"""
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
