from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import uuid

from authapp.models import PasswordReset
from authapp.forms import RegisterForm, LoginForm, PasswordResetForm, SetResetPasswordForm, PassChangeForm

from dashboard.models import Profile
from linkedin.email import send_mail



#SECTION :      Register
def register_view(request):

    #!      if user authenticated
    if request.user.is_authenticated:
        return redirect("dashboard:profile", username=request.user.username)
    
    #!         custom form edit
    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save()

            #!      send account verification link to email
            user_profile = Profile.objects.get(user=user)
            reset_link = f"http://127.0.0.1:8000/verify-account/{user.id}/{user_profile.unique_id}/"
            send_mail(subject="Verify Your Linkedin Account", text_message=reset_link, receiver_email=user.email)

            login(request=request, user=user)

            messages.success(request, "Account Register successfully. We have sent verification email please check your mail box and click on link to verify your account.")

            #ERROR :     later - redirect to profile edit form page
            return redirect("home:home")
            
    else:
        form = RegisterForm()

    context = {
        "form": form
    }

    return render(request=request, template_name="authapp/register.html", context=context)


#NOTE :     delete account
@login_required
def delete_account_view(request):
    User.objects.get(pk=request.user.id).delete()
    return redirect("authapp:register")

#SECTION:           verify user account
def verify_user_account_view(request, user_id, uuid_id):
    try:
        user = User.objects.get(pk=user_id)
    except:
        return render(request=request, template_name="error/user_not_exists.html")
    
    if Profile.objects.filter(user=user, unique_id=uuid_id).exists():
        Profile.objects.filter(user=user, unique_id=uuid_id).update(verify=True)
        messages.success(request=request, message="Your account has been verify.")
        return redirect("home:home")
    else:
        return render(request=request, template_name="error/user_not_exists.html")


#SECTION :         Login
def login_view(request):
    
    if request.user.is_authenticated:
        return redirect("dashboard:profile", username=request.user.username)
    
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request=request, user=user)
                
                messages.success(request, "Login success...")
                
                return redirect("home:home")
    else:
        form = LoginForm()
    
    context = {
        "form": form
    }
    
    return render(request=request, template_name="authapp/login.html", context=context)



#SECTION :         Logout
def logout_view(request):
    if not request.user.is_authenticated:
        return redirect("authapp:login")
    
    logout(request=request)
    
    return redirect("authapp:login")


#SECTION :         Login User Change Password
@login_required
def change_password_view(request):
    if request.method == "POST":
        form = PassChangeForm(user=request.user, data=request.POST)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, "Password updated")

            return redirect("authapp:login")            
        
    else:
        form = PassChangeForm(user=request.user)
    
    context = {
        "form": form
    }
    
    return render(request=request, template_name="authapp/change-password.html", context=context)



#SECTION :     email send pass reset
def email_send_pass_reset_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard:profile", username=request.user.username)

    #   take email or username from user
    if request.method == "POST":
        form = PasswordResetForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]

            if not User.objects.filter(email=email).exists():
                return render(request=request, template_name="error/user_not_exists.html")

            user = User.objects.get(email=email)
            unique_id = uuid.uuid4()

            if PasswordReset.objects.filter(user=user).exists():
                PasswordReset.objects.filter(user=user).update(uuid_id=unique_id)
            else:
                PasswordReset.objects.create(user=user, uuid_id=unique_id)

            reset_link = f"http://127.0.0.1:8000/reset-password/{user.id}/{unique_id}/"
            print(user.id)
            print(user.email)
            send_mail(subject="Password Reset", text_message=reset_link, receiver_email=user.email)

            return render(request=request, template_name="authapp/sent_reset_password.html")

    else:
        form = PasswordResetForm(request.POST)

    context = {
        "form": form
    }

    return render(request=request, template_name="authapp/email_send_pass_reset.html", context=context)


#SECTION :     forget password - reset password
def reset_password_view(request, user_id, uuid_id):
    if request.user.is_authenticated:
        return redirect("dashboard:profile", username=request.user.username)
    
    try:
        user = User.objects.get(pk=user_id)
    except:
        return render(request=request, template_name="error/user_not_exists.html")

    if PasswordReset.objects.filter(user=user, uuid_id=uuid_id):
        if request.method == "POST":
            form = SetResetPasswordForm(user=user, data=request.POST)
            if form.is_valid():
                form.save()
                PasswordReset.objects.filter(user=user).update(uuid_id="")
                messages.success(request, "Password updated")

                return redirect("authapp:login")
        else:
            form = SetResetPasswordForm(user=user)
    else:
        return render(request=request, template_name="error/user_not_exists.html")
    
    
    context = {
        "form": form
    }

    return render(request=request, template_name="authapp/reset_password_view.html", context=context)