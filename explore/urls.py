from django.urls import path

from explore.views import explore_view, search_user_view


app_name = "explore"

urlpatterns = [
    path("", view=explore_view, name="explore"),
    path("search/", view=search_user_view, name="search_user"),
]
