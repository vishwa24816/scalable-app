from rest_framework import permissions

class IsSystemAdmin(permissions.BasePermission):
    """
    Allows access only to system administrators.
    """
    def has_permission(self, request, view):
        return bool(
            request.user and 
            request.user.is_authenticated and 
            request.user.role == 'SYSTEM_ADMINISTRATOR'
        )

class IsTeamMember(permissions.BasePermission):
    """
    Allows access to team members and system administrators.
    """
    def has_permission(self, request, view):
        return bool(
            request.user and 
            request.user.is_authenticated and 
            request.user.role in ['TEAM_MEMBER', 'SYSTEM_ADMINISTRATOR']
        )
