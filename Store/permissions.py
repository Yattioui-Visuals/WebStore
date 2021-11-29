from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Permission to only allow owners of an object to edit it.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or obj.buyer.user == request.user


class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    Allows full access only to admin users.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


class IsAdminUserOrOwner(permissions.BasePermission):
    """
    Allows access to admin users or owners.
    """
    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_staff or obj.user == request.user)


class IsAdminUserOrOwnerOrder(permissions.BasePermission):
    """
    Allows access to admin users or owners for orders.
    """

    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_staff or obj.buyer.user == request.user)
