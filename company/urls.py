from django.urls import path

from company.views import create_page_view, detail_page_view, edit_page_view, delete_page_view, create_job_view, page_list_view, list_job_view, detail_job_view, edit_job_view, delete_job_view, apply_job_view, applied_your_job_list_view, save_job_view, saved_job_list_view, follow_page_view, follow_page_list_view


app_name = "company"


urlpatterns = [
    path("list/", view=page_list_view, name="page_list"),
    path("create/", view=create_page_view, name="create_page"),
    path("detail/<int:page_id>/", view=detail_page_view, name="detail_page"),
    path("edit/<int:page_id>/", view=edit_page_view, name="edit_page"),
    path("delete/<int:page_id>/", view=delete_page_view, name="delete_page"),

    path("follow/<int:page_id>/", view=follow_page_view, name="follow_page"),
    path("follow/list/", view=follow_page_list_view, name="follow_page_list"),

    path("job/", view=list_job_view, name="list_job"),
    path("job/create/<int:page_id>/", view=create_job_view, name="create_job"),
    path("job/detail/<int:job_id>/", view=detail_job_view, name="detail_job"),
    path("job/edit/<int:job_id>/", view=edit_job_view, name="edit_job"),
    path("job/delete/<int:job_id>/", view=delete_job_view, name="delete_job"),
    path("job/apply/<int:job_id>/", view=apply_job_view, name="apply_job"),

    path("job/applied/", view=applied_your_job_list_view, name="applied_job_list"),

    path("job/save/<int:job_id>/", view=save_job_view, name="save_job"),
    path("job/saved/", view=saved_job_list_view, name="saved_job_list"),
]
