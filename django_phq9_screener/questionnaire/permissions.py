# External
from rest_framework import permissions

# Local
from .models import PHQ9Answer

class PHQ9AnswerPermissions(permissions.DjangoModelPermissions):
    def has_object_permission(self, request, view, obj):
        validated = super().has_object_permission(request, view, obj)
        if not validated:
            return False

        return obj.user == request.user
