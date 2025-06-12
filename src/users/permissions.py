from rest_framework import permissions

class IsUserOwnerorGetandPostOnly(permissions.BasePermission):
    
    # '''''''
    # custom permissio for userviewset to only allow users to edit their own profile otherwise, Get and Post only
    # '''''
    def has_permission(self, request, view):
        return True
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if not request.user.is_anonymous:
            return request.user==obj
        
        return False
    
    