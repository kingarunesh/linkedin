from django.contrib import admin

from home.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "subject", "message", "created_date", "review"]