from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, SetPasswordForm, PasswordChangeForm
from django.contrib.auth.models import User



#SECTION :          register form
class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}), label="Confirm Password")
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control", "required": True}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "required": True}),
            "email": forms.EmailInput(attrs={"class": "form-control", "required": True}),
        }


#SECTION :          login form
class LoginForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}), label="Password")
    username = UsernameField(widget=forms.TextInput(attrs={"class": "form-control"}))
    class Meta:
        model = User
        fields = "__all__"


#SECTION :          password reset send email form
class PasswordResetForm(forms.Form):
    email = forms.EmailField(max_length=250, widget=forms.EmailInput(attrs={"class": "form-control"}), label="Email Address")


#SECTION :          reset password form
class SetResetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}), label="Password")
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}), label="Confirm Password")
    class Meta:
        model = User


#SECTION :          change password form
class PassChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control mb-3"}), label="Old Password")
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control mb-3"}), label="New Password")
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control mb-3"}), label="New Confirm Password")
    class Meta:
        model = User