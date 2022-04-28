from rest_framework import serializers
from django.core import exceptions
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for a user"""
    password = serializers.CharField(write_only=True)

    def validate_password(self, password):
        try:
            validate_password(password)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return password

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ('email', 'role', 'password', )
