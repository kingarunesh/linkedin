from django.contrib import admin



from dashboard.models import Profile, Skill, Education, Experience, Project, ProfileView, FollowerFollowing, Language, BlockUser, ResumeFile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "headline", "gender", "dob", "account_type", "verify", "updated_date"]
    list_display_links = ["id", "user", "headline", "gender", "dob", "account_type", "verify", "updated_date"]



@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "skill", "skill_category", "created_date"]
    list_display_links = ["id", "user", "skill", "skill_category", "created_date"]



@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "school", "degree", "grade"]
    list_display_links = ["id", "user", "school", "degree", "grade"]


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "job_title", "compnay_name", "updated_date"]
    list_display_links = ["id", "user", "job_title", "compnay_name", "updated_date"]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "title", "start_date", "updated_date"]
    list_display_links = ["id", "user", "title", "start_date", "updated_date"]



@admin.register(ProfileView)
class ProfileViewAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "visited_user", "visited_datetime"]
    list_display_links = ["id", "user", "visited_user", "visited_datetime"]


@admin.register(FollowerFollowing)
class FollowerFollowingAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "following"]
    list_display_links = ["id", "user", "following"]


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "lang"]



@admin.register(BlockUser)
class BlockUserAdmin(admin.ModelAdmin):
    list_display = ["id", "blocker_user", "blocked_user", "block_date"]
    list_display_links = ["id", "blocker_user", "blocked_user", "block_date"]



@admin.register(ResumeFile)
class ResumeFileAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "resume", "created_date", "last_updated"]
    list_display_links = ["id", "user", "resume", "created_date", "last_updated"]