from django.db import models
from django.conf import settings

class Reward(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reward_name = models.CharField(max_length=255)
    required_points = models.IntegerField()

    def __str__(self):
        return self.reward_name