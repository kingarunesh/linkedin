from django.db import models

from django.contrib.auth.models import User


import uuid


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    image1 = models.ImageField(upload_to="posts/post", null=True, blank=True, default="post.jpg")
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    unique_id = models.UUIDField(default=uuid.uuid4)
    active = models.BooleanField(default=True)

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookmark_user")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="bookmark_post")
    created_date = models.DateTimeField(auto_now_add=True)


class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="like_user_post")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="like_post")
    created_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_user")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment_post")
    text = models.CharField(max_length=250, default="")
    created_date = models.DateTimeField(auto_now_add=True)


# class Poll(models.Model):
#     user = models.ForeignKey(User, on_delete=models.PROTECT)
#     question = models.CharField(max_length=250)
#     a_option = models.CharField(max_length=50)
#     b_option = models.CharField(max_length=50)
#     c_option = models.CharField(max_length=50)
#     d_option = models.CharField(max_length=50)

#     updated_date = models.DateTimeField(auto_now=True)
#     created_date = models.DateTimeField(auto_now_add=True)