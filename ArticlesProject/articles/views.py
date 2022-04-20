from rest_framework import generics
from .serializers import ArticleSerializer
from .models import Article
from .permissions import IsOwnerOrReadOnly, IsAuthorOrReadOnly, IsPublicArticleAndAnonymUser


class ArticleListCreateView(generics.ListCreateAPIView):
    """View for article list getting or article creating"""
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        user = self.request.user
        if user.id is None:
            return Article.objects.filter(type=1)
        return Article.objects.all()


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View for article getting, updating, deleting"""
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsPublicArticleAndAnonymUser,)
