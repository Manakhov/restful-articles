from rest_framework import serializers
from .models import Article


class ArticlesListSerializer(serializers.ModelSerializer):
    """Serializer for articles list"""
    author = serializers.CharField()

    class Meta:
        model = Article
        fields = ('id', 'title', 'author')


class ArticleDetailSerializer(serializers.ModelSerializer):
    """Serializer for one article"""
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    author_name = serializers.CharField(read_only=True, source='author')

    class Meta:
        model = Article
        fields = '__all__'
