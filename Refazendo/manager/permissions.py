from rest_framework.permissions import BasePermission

class IsGerente(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and hasattr(request.user, 'gerente')