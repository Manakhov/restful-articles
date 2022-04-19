from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    """Serializer for an article"""
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    author_email = serializers.CharField(read_only=True, source='author')

    class Meta:
        model = Article
        fields = '__all__'
