from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_superuser


class AdminPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff and request.user.is_active:
            return request.user.groups.filter(name='Admin').exists()
        return False


class SalesPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff and request.user.is_active:
            return request.user.groups.filter(name='Equipe de vente').exists()
        return False

    def has_object_permission(self, request, view, obj):
        return request.user == obj.sales_contact


class SupportPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff and request.user.is_active:
            return request.user.groups.filter(name='Equipe support').exists()
        return False

    def has_object_permission(self, request, view, obj):
        return request.user == obj.support_contact
