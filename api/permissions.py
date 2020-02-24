from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if hasattr(obj, 'registered_by'):
            return obj.registered_by == request.user

        return obj.user == request.user


class IsMySelf(permissions.BasePermission):
    """
    Custom permission to only allow User to edit himself
    """

    def has_object_permission(self, request, view, obj):
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        return obj == request.user
