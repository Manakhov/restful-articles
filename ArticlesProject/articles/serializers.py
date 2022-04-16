from rest_framework import serializers
from .models import Article


class ArticlesListSerializer(serializers.ModelSerializer):
    """Serializer for articles list"""
    class Meta:
        model = Article
        fields = ('id', 'title', 'author')


class ArticleDetailSerializer(serializers.ModelSerializer):
    """Serializer for one article"""
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Article
        fields = '__all__'
