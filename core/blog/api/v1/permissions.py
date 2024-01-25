from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    This is permission to only allow author to edit
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.author.user == request.user