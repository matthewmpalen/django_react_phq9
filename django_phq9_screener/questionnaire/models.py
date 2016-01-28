# Django
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

class PHQ9Answer(models.Model):
    ANSWER_CHOICES = (
        (0, _('Not at all')), 
        (1, _('Several days')), 
        (2, _('More than half the days')), 
        (3, _('Nearly every day'))
    )

    user = models.ForeignKey(User)

    little_interest = models.PositiveSmallIntegerField(choices=ANSWER_CHOICES, 
        default=0, 
        verbose_name=_('Little interest or pleasure in doing things?'))

    depression = models.PositiveSmallIntegerField(choices=ANSWER_CHOICES, 
        default=0, 
        verbose_name=_('Feeling down, depressed, or hopeless?'))

    sleep_issues = models.PositiveSmallIntegerField(choices=ANSWER_CHOICES, 
        default=0, 
        verbose_name=_('Trouble falling or staying asleep, or sleeping too much?'))
    
    lethargy = models.PositiveSmallIntegerField(choices=ANSWER_CHOICES, 
        default=0, 
        verbose_name=_('Feeling tired or having little energy?'))

    appetite_issues = models.PositiveSmallIntegerField(choices=ANSWER_CHOICES, 
        default=0, 
        verbose_name=_('Poor appetite or overeating?'))

    shame = models.PositiveSmallIntegerField(choices=ANSWER_CHOICES, 
        default=0, 
        verbose_name=_('Feeling bad about yourself -- or that you are a failure or have let yourself or your family down?'))

    concentration_issues = models.PositiveSmallIntegerField(
        choices=ANSWER_CHOICES, 
        default=0, 
        verbose_name=_('Trouble concentrating on things, such as reading the newspaper or watching television?'))

    activity_change = models.PositiveSmallIntegerField(choices=ANSWER_CHOICES, 
        default=0, 
        verbose_name=_('Moving or speaking so slowly that other people could have noticed? Or the opposite -- being so fidgety or restless that you have been moving around a lot more than usual?'))

    suicidal_thoughts = models.PositiveSmallIntegerField(
        choices=ANSWER_CHOICES, 
        default=0, 
        verbose_name=_('Thoughts that you would be better off dead, or of hurting yourself in some way?'))

    depression_severity = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} - {1}'.format(self.user, self.updated_at)

    def save(self, *args, **kwargs):
        severity = self.little_interest
        severity += self.depression
        severity += self.sleep_issues
        severity += self.lethargy
        severity += self.appetite_issues
        severity += self.shame
        severity += self.concentration_issues
        severity += self.activity_change
        severity += self.suicidal_thoughts

        if severity > 27:
            raise ValueError('Valid score range: 0 - 27')

        self.depression_severity = severity
        super().save(*args, **kwargs)

    def severity(self):
        if self.depression_severity < 5:
            return 'None'
        elif self.depression_severity < 10:
            return 'Mild'
        elif self.depression_severity < 15:
            return 'Moderate'
        elif self.depression_severity < 20:
            return 'Moderately Severe'
        elif self.depression_severity < 28:
            return 'Severe'
        else:
            return ''
