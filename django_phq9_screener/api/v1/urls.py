# Django
from django.conf.urls import include, url

# Local
from django_phq9_screener.django_auth.urls import router as django_auth_router
from django_phq9_screener.questionnaire.urls import router as q_router

urlpatterns = [
    url(r'', include(django_auth_router.urls)), 
    url(r'^questionnaire/', include(q_router.urls))
]
