from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .serializers import ArticleSerializer
from .models import Article
from .permissions import IsOwnerOrReadOnly, IsAuthorOrReadOnly, IsPublicArticleAndAnonymUser


# class ArticleListCreateView(generics.ListCreateAPIView):
#     """View for article list getting or article creating"""
#     serializer_class = ArticleSerializer
#     permission_classes = (IsAuthorOrReadOnly,)
#
#     def get_queryset(self):
#         user = self.request.user
#         if user.id is None:
#             return Article.objects.filter(type=1)
#         return Article.objects.all()
#
#
# class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
#     """View for article getting, updating, deleting"""
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()
#     permission_classes = (IsOwnerOrReadOnly, IsPublicArticleAndAnonymUser,)


class ArticleViewSet(viewsets.ViewSet):
    """ViewSet for article"""

    def list(self, request):
        queryset = Article.objects.all()
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
