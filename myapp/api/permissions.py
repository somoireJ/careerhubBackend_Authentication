from rest_framework.permissions import BasePermission


class IsApplicantUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_applicant)


class IsEmployerUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_employer)


# class IsAdminUser(BasePermission):
#     def has_permission(self, request, view):
#         return bool(request.user and request.user.is_admin)
