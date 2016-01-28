# Django
from django.views.generic import TemplateView

class HomepageView(TemplateView):
    template_name = 'homepage.html'

class PHQ9ScreenerView(TemplateView):
    template_name = 'phq9_screener.html'
