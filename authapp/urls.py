from django.urls import path

from authapp.views import register_view, login_view, logout_view, change_password_view, reset_password_view, email_send_pass_reset_view, verify_user_account_view, delete_account_view


app_name = "authapp"

urlpatterns = [    
    path("register/", view=register_view, name="register"),
    path("delete-account/", view=delete_account_view, name="delete_account"),
    path("login/", view=login_view, name="login"),
    path("logout/", view=logout_view, name="logout"),
    path("change-password/", view=change_password_view, name="change_password"),
    path("send-email/", view=email_send_pass_reset_view, name="email_send_pass_reset_view"),
    path("reset-password/<int:user_id>/<str:uuid_id>/", view=reset_password_view, name="reset_password_view"),
    path("verify-account/<int:user_id>/<str:uuid_id>/", view=verify_user_account_view, name="verify_user_account"),
]
