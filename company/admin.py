from django.contrib import admin

from company.models import Page, PageFollower, Job, AppliedJob, SavedJob


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "name", "created_date"]
    list_display_links = ["id", "user", "name", "created_date"]


@admin.register(PageFollower)
class PageFollowerAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "page", "created_date"]
    list_display_links = ["id", "user", "page", "created_date"]



@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "company", "job_title", "till_apply", "created_date"]
    list_display_links = ["id", "user", "company", "job_title", "till_apply", "created_date"]


@admin.register(AppliedJob)
class AppliedJobAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "job", "applied_date"]
    list_display_links = ["id", "user", "job", "applied_date"]


@admin.register(SavedJob)
class SavedJobAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "job", "saved_date"]
    list_display_links = ["id", "user", "job", "saved_date"]
