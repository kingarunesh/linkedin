from django.contrib import admin

from notification.models import FollowNotification


@admin.register(FollowNotification)
class FollowNotificationAdmin(admin.ModelAdmin):
    list_display = ["id", "s_user", "r_user", "follow_request", "noti_date", "accepted_date"]
    list_display_links = ["id", "s_user", "r_user", "follow_request", "noti_date", "accepted_date"]