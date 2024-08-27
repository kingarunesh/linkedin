from django.contrib import admin

from authapp.models import PasswordReset


@admin.register(PasswordReset)
class PasswordResetAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "uuid_id", "first_reset", "last_reset"]
    list_display_links = ["id", "user", "uuid_id", "first_reset", "last_reset"]