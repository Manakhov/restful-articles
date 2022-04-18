from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Returns True if the method is safe or the user is the article author"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user