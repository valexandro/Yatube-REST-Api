from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Разрешает редактирование только владельцу объекта.
    У объекта должно быть поле author.
    """

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class ReadOnly(permissions.BasePermission):
    """Дает доступ к списку объектов только для чтения без аутентификации."""

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
