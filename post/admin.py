from django.contrib import admin

from post.models import Post, PostLike, Bookmark, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "last_updated", "active"]
    list_display_links = ["id", "user", "last_updated", "active"]



@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "post", "created_date"]
    list_display_links = ["id", "user", "post", "created_date"]


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "post", "created_date"]
    list_display_links = ["id", "user", "post", "created_date"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "post", "text", "created_date"]
    list_display_links = ["id", "user", "post", "text", "created_date"]