from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from post.models import Post, PostLike, Comment

from dashboard.models import FollowerFollowing
from company.models import Page, PageFollower, Job


@login_required
def home_view(request):
    #NOTE :         following user posts
    # https://stackoverflow.com/questions/53803106/django-query-how-to-find-all-posts-from-people-you-follow
    #& ( i took from stackoverflow )
    #!      get users
    following_user = FollowerFollowing.objects.filter(user=request.user, accepted=True).values("following")

    #!      find user following user post
    posts = Post.objects.filter(user__in=following_user).order_by("-last_updated")

    #NOTE :     following page jobs
    following_page = PageFollower.objects.filter(user=request.user).values("page")
    jobs = Job.objects.filter(company__in=following_page)


    context = {
        "posts": posts,
        "jobs": jobs
    }

    return render(request=request, template_name="home/home.html", context=context)