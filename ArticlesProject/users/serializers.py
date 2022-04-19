from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for a user"""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'role', 'password', )
