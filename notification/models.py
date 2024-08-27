from django.db import models
from django.contrib.auth.models import User
import uuid

from dashboard.models import FollowerFollowing


class FollowNotification(models.Model):
    s_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="s_notification_user")
    r_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="r_notification_user")
    follow_request = models.ForeignKey(FollowerFollowing, on_delete=models.CASCADE, related_name="notification_follow_req")
    noti_date = models.DateTimeField(auto_now_add=True)
    accepted_date = models.DateTimeField(auto_now=True)
    unique_id = models.UUIDField(default=uuid.uuid4, null=True, blank=True)