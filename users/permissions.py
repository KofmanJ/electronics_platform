from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    """Права доступа для модератора"""

    message = "Вы не являетесь модератором"

    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderator').exists()


class IsOwner(BasePermission):
    """Права доступа для владельца объекта"""

    message = "Вы не владелец данного объекта"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.creation_user:
            return request.method in ('GET', 'PUT', 'PATCH', 'DELETE')
        return False


class IsSuperUser(BasePermission):
    """Права доступа для администратора"""

    message = "Вы не являетесь администратором"

    def has_permission(self, request, view):
        return request.user.is_superuser


class IsUserOwner(BasePermission):
    """Права доступа для пользователя"""

    message = "Вы не являетесь владельцем этой учетной записи"

    def has_object_permission(self, request, view, obj):
        return request.user == obj
