import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for a user"""
    password = serializers.CharField(write_only=True)

    def validate_password(self, password):
        if len(password) < 8:
            raise serializers.ValidationError("Пароль должен быть не короче 8 символов.")
        elif not bool(re.search(r'\d', password)):
            raise serializers.ValidationError("Пароль должен содержать хотя бы одну цифру.")
        elif not bool(re.search(r'[a-zA-Z]', password)):
            raise serializers.ValidationError("Пароль должен содержать хотя бы одну букву любого регистра.")

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ('email', 'role', 'password', )
