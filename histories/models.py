from django.db import models
from django.conf import settings
from actions.models import Action
from rewards.models import Reward

class History(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.SET_NULL, null=True, blank=True)
    reward = models.ForeignKey(Reward, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    point_change = models.IntegerField()
    current_total_points = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.action:
            return f"{self.user.username} - {self.action.action_name} - {self.date}"
        elif self.reward:
            return f"{self.user.username} - {self.reward.reward_name} - {self.date}"
        else:
            return f"{self.user.username} - {self.date}"