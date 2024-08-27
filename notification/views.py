from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from notification.models import FollowNotification


@login_required
def notification_view(request):
    if not request.user.is_authenticated:
        return redirect("authapp:login")

    follow_notification = FollowNotification.objects.filter(r_user=request.user)

    print(follow_notification)

    context = {
        "follow_notification": follow_notification,
    }

    return render(request=request, template_name="notification/notification.html", context=context)