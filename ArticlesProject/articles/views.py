from django.shortcuts import render
from rest_framework import generics
from .serializers import ArticleDetailSerializer, ArticlesListSerializer
from .models import Article


class ArticleCreateView(generics.CreateAPIView):
    serializer_class = ArticleDetailSerializer


class ArticlesListView(generics.ListAPIView):
    serializer_class = ArticlesListSerializer
    queryset = Article.objects.all()
