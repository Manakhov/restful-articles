from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    """Returns True if the user is an author"""
    def has_permission(self, request, view):
        if request.user.id is None:
            return False
        return request.user.role == 2


class IsOwner(permissions.BasePermission):
    """Returns True if the user is the article author"""
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
