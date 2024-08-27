from django.urls import path

from dashboard.views import public_profile_view, follow_user_view, follow_accept_view, edit_profile_view, education_add_view, education_edit_view, education_delete_view, experience_delete_view, experience_edit_view, experience_add_view, project_add_view, project_edit_view, project_delete_view, skill_add_view, skill_delete_view, skill_edit_view, language_add_view, language_delete_view, language_edit_view, dashboard_view, block_unblock_user_view, profile_view_list_view, upload_resume_view


app_name = "dashboard"

urlpatterns = [
    path("user/<str:username>/", view=public_profile_view, name="profile"),
    path("edit-profile/", view=edit_profile_view, name="edit_profile"),

    path("block/<str:username>/", view=block_unblock_user_view, name="block_unblock_user"),
    
    path("follow/<str:user_id>/", view=follow_user_view, name="follow_user"),
    path("accept-request/<str:request_user>/", view=follow_accept_view, name="follow_accept"),

    path("education/add/", view=education_add_view, name="education_add"),
    path("education/edit/<int:edu_id>/", view=education_edit_view, name="education_edit"),
    path("education/delete/<int:edu_id>/", view=education_delete_view, name="education_delete"),

    path("experience/add/", view=experience_add_view, name="experience_add"),
    path("experience/edit/<int:exp_id>/", view=experience_edit_view, name="experience_edit"),
    path("experience/delete/<int:exp_id>/", view=experience_delete_view, name="experience_delete"),

    path("project/add/", view=project_add_view, name="project_add"),
    path("project/edit/<int:pro_id>/", view=project_edit_view, name="project_edit"),
    path("project/delete/<int:pro_id>/", view=project_delete_view, name="project_delete"),

    path("skill/add/", view=skill_add_view, name="skill_add"),
    path("skill/edit/<int:skill_id>/", view=skill_edit_view, name="skill_edit"),
    path("skill/delete/<int:skill_id>/", view=skill_delete_view, name="skill_delete"),

    path("language/add/", view=language_add_view, name="language_add"),
    path("language/edit/<int:language_id>/", view=language_edit_view, name="language_edit"),
    path("language/delete/<int:language_id>/", view=language_delete_view, name="language_delete"),
    
    path("dashboard/", view=dashboard_view, name="dashboard"),

    path("profile-view/", view=profile_view_list_view, name="profile_view_list"),

    path("upload-resume/", view=upload_resume_view, name="upload_resume"),
]
