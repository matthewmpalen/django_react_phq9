# External
from rest_framework.serializers import HyperlinkedModelSerializer

# Local
from .models import PHQ9Answer

class PHQ9AnswerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = PHQ9Answer
        read_only_fields = ('user', 'depression_severity')
