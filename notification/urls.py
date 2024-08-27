from django.urls import path

from notification.views import notification_view


app_name = "notification"

urlpatterns = [
    path("", view=notification_view, name="notification")
]
