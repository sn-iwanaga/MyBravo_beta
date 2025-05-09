from django.db import models
from django.conf import settings

class Action(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    action_name = models.CharField(max_length=255)
    points = models.IntegerField()

    def __str__(self):
        return self.action_name