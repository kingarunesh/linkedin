from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from post.models import Post, PostLike, Comment, Bookmark
from post.forms import CommnetForm, PostForm

from dashboard.models import BlockUser, FollowerFollowing


#SECTION :          list post
@login_required
def list_post_view(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        return render(request=request, template_name="error/404.html", context={"message": "User does not exists"})
    
    #!      if post user blocked then do not display post
    if BlockUser.objects.filter(blocker_user=user, blocked_user=request.user).exists():
        return render(request=request, template_name="error/404.html", context={"message": "Invalid request"})

    posts = Post.objects.filter(user=user)

    context = {
        "posts": posts
    }

    return render(request=request, template_name="post/list_post.html", context=context)


#SECTION :          saved list post
@login_required
def saved_list_post_view(request):

    bookmarks = Bookmark.objects.filter(user=request.user)

    context = {
        "bookmarks": bookmarks
    }

    return render(request=request, template_name="post/saved_list_post.html", context=context)


#SECTION :          add new post
@login_required
def add_post_view(request):
    #NOTE :         post form
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = Post.objects.create(
                user=request.user,
                description=form.cleaned_data["description"],
                image1=form.cleaned_data["image1"]
            )
            return redirect("post:detail_post", post_id=post.id)
    else:
        form = PostForm()

    context = {
        "form": form,
    }

    return render(request=request, template_name="post/add_post.html", context=context)


#SECTION :         post details
@login_required
def detail_post_view(request, post_id):
    #NOTE :         post
    post = Post.objects.get(pk=post_id)

    #!      if post user blocked then do not display post
    if BlockUser.objects.filter(blocker_user=post.user, blocked_user=request.user).exists():
        return render(request=request, template_name="error/404.html", context={"message": "Invalid request"})


    #NOTE :         like post
    like_post = PostLike.objects.filter(post=post, user=request.user)

    #NOTE :         bookmark post
    bookmark_post = Bookmark.objects.filter(post=post, user=request.user)

    #NOTE :         comments
    comments = Comment.objects.filter(post=post)

    #!             comment form
    if request.method == "POST":
        form = CommnetForm(request.POST)

        if form.is_valid():
            Comment.objects.create(
                post=post,
                user=request.user,
                text=form.cleaned_data["text"]
            )
            return redirect("post:detail_post", post_id=post_id)
    else:
        form = CommnetForm()


    context = {
        "post": post,
        "like_post": like_post,
        "bookmark_post": bookmark_post,
        "comments": comments,
        "form": form
    }

    return render(request=request, template_name="post/post_details.html", context=context)



#SECTION :         like post
@login_required
def post_like_view(request, post_id):
    #!      if user already liked post then delete
    if PostLike.objects.filter(user=request.user, post=post_id).exists():
        PostLike.objects.filter(user=request.user, post=post_id).delete()
    else:
        #!      if user not liked post then create new like
        post = Post.objects.get(pk=post_id)
        PostLike.objects.create(
            user=request.user,
            post=post
        )
    
    return redirect("post:detail_post", post_id=post_id)


#SECTION :          Bookmark
@login_required
def bookmark_post_view(request, post_id):
    post = Post.objects.get(pk=post_id)

    if not Bookmark.objects.filter(user=request.user, post=post).exists():
        Bookmark.objects.create(user=request.user, post=post)
    else:
        Bookmark.objects.filter(post=post, user=request.user).delete()
    
    return redirect("post:detail_post", post_id=post_id)



#SECTION :          edit post
@login_required
def edit_post_view(request, post_id):
    post = Post.objects.get(pk=post_id)

    #!      only created user can edit post
    if request.user != post.user:
        return render(request=request, template_name="error/404.html", context={"message": "Invalid request"})

    if request.method == "POST":
        
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect("post:detail_post", post_id=post.id)
    else:
        form = PostForm(instance=post)
    
    context = {
        "form": form
    }

    return render(request=request, template_name="post/edit_post.html", context=context)


#SECTION :          delete post
@login_required
def post_delete_view(request, post_id):
    post = Post.objects.get(pk=post_id)

    if request.user != post.user:
        return render(request=request, template_name="error/404.html", context={"message": "Invalid request"})
    
    post.delete()

    return redirect("home:home")