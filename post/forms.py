from django import forms

from post.models import Post, Comment



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["description", "image1"]

        labels = {
            "image1": "Image"
        }

        widgets = {
            "description": forms.Textarea(attrs={"class": "form-control mb-3", "rows": 3}),
            "image1": forms.FileInput(attrs={"class": "form-control mb-3"})
        }
    


class CommnetForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]

        labels = {
            "text": "Comment"
        }

        widgets = {
            "text": forms.Textarea(attrs={"class": "form-control w-2", "rows": 3})
        }