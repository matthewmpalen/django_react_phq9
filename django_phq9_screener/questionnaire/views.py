# External
from rest_framework import viewsets

# Local
from .models import PHQ9Answer
from .permissions import PHQ9AnswerPermissions
from .serializers import PHQ9AnswerSerializer

###########
# ViewSets
###########

class PHQ9AnswerViewSet(viewsets.ModelViewSet):
    queryset = PHQ9Answer.objects.all()
    serializer_class = PHQ9AnswerSerializer
    permission_classes = (PHQ9AnswerPermissions,)

    def get_queryset(self):
        if self.request.user.is_anonymous():
            return PHQ9Answer.objects.none()

        return PHQ9Answer.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
