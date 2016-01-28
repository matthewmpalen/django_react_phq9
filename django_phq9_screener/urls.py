# Django
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

# Local
from .views import HomepageView, PHQ9ScreenerView

urlpatterns = [
    url(r'^$', HomepageView.as_view(), name='home'), 
    url(r'^admin/', admin.site.urls), 
    url(r'^api-auth/', include('rest_framework.urls', 
        namespace='rest_framework')), 
    url(r'^api/v1/', include('django_phq9_screener.api.v1.urls')), 
    url(r'^phq9_screener/$', PHQ9ScreenerView.as_view(), name='phq9_screener')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
