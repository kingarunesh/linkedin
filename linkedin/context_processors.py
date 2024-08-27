from pprint import pprint

from django.contrib.auth.models import User

from dashboard.models import Profile

from notification.models import FollowNotification


def current_user_profile_fun(request):
    try:
        current_user = User.objects.get(id=request.user.id)
        current_user_profile = Profile.objects.get(user_id=request.user.id)
        verify_user = Profile.objects.get(user=request.user).verify
    except:
        current_user_profile = None
        current_user = None
        verify_user = None

    total_notification = FollowNotification.objects.all().count()

    context = {
        "current_user_profile": current_user_profile,
        "current_user": current_user,
        "verify_user": verify_user,
        "total_notification": total_notification
    }

    return context