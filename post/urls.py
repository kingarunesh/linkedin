from django.urls import path

from post.views import post_like_view, post_delete_view, detail_post_view, bookmark_post_view, edit_post_view, list_post_view, add_post_view, saved_list_post_view


app_name = "post"

urlpatterns = [
    path("new/", view=add_post_view, name="add_post"),
    path("user/<str:username>/", view=list_post_view, name="list_post"),
    path("saved/", view=saved_list_post_view, name="saved_list_post"),
    path("<int:post_id>/", view=detail_post_view, name="detail_post"),
    path("edit/<post_id>/", view=edit_post_view, name="edit_post"),
    path("delete/<post_id>/", view=post_delete_view, name="post_delete"),
    
    path("like/<post_id>/", view=post_like_view, name="post_like"),
    path("bookmark/<post_id>/", view=bookmark_post_view, name="bookmark_post"),
]
