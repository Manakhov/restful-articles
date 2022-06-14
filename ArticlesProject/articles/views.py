from rest_framework import viewsets
from .serializers import ArticleSerializer
from .models import Article
from .permissions import IsAuthor, IsOwner


class ArticleViewSet(viewsets.ModelViewSet):
    """ViewSet for article"""
    serializer_class = ArticleSerializer

    def get_permissions(self):
        permission_classes = ()
        if self.action == 'create':
            permission_classes = (IsAuthor,)
        elif self.action == 'update' or self.action == 'destroy':
            permission_classes = (IsOwner,)
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        """Getting all articles if the user is a subscriber"""
        if self.action == 'list' or self.action == 'retrieve':
            user = self.request.user
            if user.id is None or user.role == 2:
                return Article.objects.filter(type=1)
        return Article.objects.all()
