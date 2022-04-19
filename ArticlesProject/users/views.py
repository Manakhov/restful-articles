from rest_framework import generics
from .serializers import UserSerializer


class UserCreateView(generics.CreateAPIView):
    """View for user creating"""
    serializer_class = UserSerializer

