# Django
from django.contrib import admin

# Local
from .models import PHQ9Answer

class PHQ9AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'depression_severity', 'created_at', 'updated_at')
    list_filter = ('little_interest', 'depression', 'sleep_issues', 
        'lethargy', 'appetite_issues', 'shame', 'concentration_issues', 
        'activity_change', 'suicidal_thoughts', 'depression_severity')

admin.site.register(PHQ9Answer, PHQ9AnswerAdmin)
