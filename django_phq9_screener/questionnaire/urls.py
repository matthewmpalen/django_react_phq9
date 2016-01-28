# External
from rest_framework import routers

# Local
from .views import PHQ9AnswerViewSet

router = routers.SimpleRouter()
router.register(r'phq9answers', PHQ9AnswerViewSet)
