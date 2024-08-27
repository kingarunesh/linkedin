from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User


from dashboard.models import Profile, FollowerFollowing, Education, Experience, Skill, ProfileView, Language, Project, BlockUser, ResumeFile
from dashboard.forms import AEditProfileForm, BEditProfileForm, EducationForm, ExperienceForm, ProjectForm, SkillForm, LanguageForm, ResumeFileForm

from post.models import Post, Bookmark
from company.models import Page, AppliedJob, SavedJob, PageFollower

from notification.models import FollowNotification



#SECTION :          dashboard
@login_required
def dashboard_view(request):
    return render(request=request, template_name="dashboard/dashboard.html")


#SECTION :         profile
@login_required
def public_profile_view(request, username):
    #NOTE:   check using username user exits or not
    try:
        user = User.objects.get(username=username)
    except:
        return render(request=request, template_name="error/404.html")


    #NOTE :         check user is blocked or not
    if BlockUser.objects.filter(blocker_user=user, blocked_user=request.user).exists():
        return render(request=request, template_name="error/404.html", context={"message": "The user you looking for does not exists"})
    
    #!      pass context blocked or not
    blocked = None
    if request.user != user:
        blocked = BlockUser.objects.filter(blocker_user=request.user, blocked_user=user).exists()
    else:
        blocked = False
    
    #NOTE :         account type ( public or private )
    user_profile = None

    #   login user view can view own profile with no condition 
    if request.user == user:
        user_profile = Profile.objects.get(user=user)

        #   if user profile is public then display everything
    elif Profile.objects.get(user=user).account_type == "Public":
        user_profile = Profile.objects.get(user=user)

        #!      user=profile_user & visited_user=current_login_user_visiting
        ProfileView.objects.create(user=user, visited_user=request.user)

        #   if user profile is private
    elif Profile.objects.get(user=user).account_type == "Private":
        #    but following that user and user have accepted follow request then display
        if FollowerFollowing.objects.filter(user=request.user, following=user, accepted=True).exists():
            user_profile = Profile.objects.get(user=user)

            #!      user=profile_user & visited_user=current_login_user_visiting
            ProfileView.objects.create(user=user, visited_user=request.user)
        else:

            #!      user=profile_user & visited_user=current_login_user_visiting
            ProfileView.objects.create(user=user, visited_user=request.user)
            user_profile = Profile.objects.get(user=user)
            total_followings = FollowerFollowing.objects.filter(user=user).count()
            total_followers = FollowerFollowing.objects.filter(following=user).count()
            follow_unfollow = FollowerFollowing.objects.filter(user=request.user, following=user).exists()

            context = {
                "user": user,
                "user_profile": user_profile,
                "total_followings": total_followings,
                "total_followers": total_followers,
                "follow_unfollow": follow_unfollow
            }
            return render(request=request, template_name="dashboard/private_account.html", context=context)

    #NOTE :         analytics
    #!      total profile views
    profile_view = ProfileView.objects.filter(user=user).count()
    
    #!      total posts
    total_posts = Post.objects.filter(user=user).count()


    #!      total saved post
    total_bookmark_posts = Bookmark.objects.filter(user=user).count()

    #!      total applied jobs
    applied_jobs = AppliedJob.objects.filter(user=user)

    #!      total saved jobs
    saved_jobs = SavedJob.objects.filter(user=user)

    #!      all pages
    user_pages = Page.objects.filter(user=user)
        

    #NOTE:      education
    educations = Education.objects.filter(user=user)

    #NOTE :     experience
    experiences = Experience.objects.filter(user=user)

    #NOTE :     projects
    projects = Project.objects.filter(user=user)

    #NOTE :     skills
    skills = Skill.objects.filter(user=user)

    #NOTE :     languege
    langueges = Language.objects.filter(user=user)

    #NOTE :     Following
    followings = FollowerFollowing.objects.filter(user=user)


    #NOTE :     followers
    followers = FollowerFollowing.objects.filter(following=user)  

    #NOTE :     follow & unfollow
    follow_unfollow = None
    follow_accepted = None

    if user != request.user:
        follow_unfollow = FollowerFollowing.objects.filter(user=request.user, following=user).exists()
        if follow_unfollow:
            follow_accepted = FollowerFollowing.objects.filter(user=request.user, following=user)[0].accepted
        

    context = {
        "user": user,
        "user_profile": user_profile,

        "profile_view": profile_view,
        "total_posts": total_posts,
        "total_bookmark_posts": total_bookmark_posts,
        "user_pages": user_pages,

        "applied_jobs": applied_jobs,
        "saved_jobs": saved_jobs,

        "educations": educations,
        "experiences": experiences,
        "projects": projects,
        "skills": skills,
        "langueges": langueges,

        "followings": followings,
        "total_followings": followings.count(),

        "followers": followers,
        "total_followers": followers.count(),

        "follow_unfollow": follow_unfollow,
        "follow_accepted": follow_accepted,

        "blocked": blocked,
    }
    
    return render(request=request, template_name="dashboard/profile.html", context=context)


#SECTION :          block user
def block_unblock_user_view(request, username):
    #!      check user exists or not
    try:
        user = User.objects.get(username=username)
    except:
        return render(request=request, template_name="error/404.html", context={"message": "User does not exists"})
    
    if BlockUser.objects.filter(blocker_user=request.user, blocked_user=user).exists():
        BlockUser.objects.filter(blocker_user=request.user, blocked_user=user).delete()
    else:
        BlockUser.objects.create(blocker_user=request.user, blocked_user=user)

    return redirect("dashboard:profile", username=username)


#SECTION :          edit profile
@login_required
def edit_profile_view(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        aform = AEditProfileForm(request.POST, instance=request.user)
        bform = BEditProfileForm(request.POST, request.FILES, instance=profile)
        if aform.is_valid() or bform.is_valid():
            aform.save()
            bform.save()
            return redirect("dashboard:profile", username=request.user.username)
    else:
        aform = AEditProfileForm(instance=request.user)
        bform = BEditProfileForm(instance=profile)
    
    context = {
        "aform": aform,
        "bform": bform,
    }

    return render(request=request, template_name="dashboard/edit_profile.html", context=context)



#SECTION :          Follow user
@login_required
def follow_user_view(request, user_id):
    #NOTE :     get follow user
    try:
        user = User.objects.get(pk=user_id)
    except:
        return render(request=request, template_name="error/404.html")
    
    #NOTE :     follow user
    

    #   check if user already follow then unfollow
    if FollowerFollowing.objects.filter(user=request.user, following=user).exists():
        FollowerFollowing.objects.filter(user=request.user, following=user).delete()

        if FollowNotification.objects.filter(s_user=request.user, r_user=user).exists():
            FollowNotification.objects.filter(s_user=request.user, r_user=user).delete()
    else:
        new_follow = FollowerFollowing.objects.create(user=request.user, following=user)
        FollowNotification.objects.create(s_user=request.user, r_user=user, follow_request=new_follow)
    
    return redirect("dashboard:profile", username=user.username)




#SECTION :          request accept
@login_required
def follow_accept_view(request, request_user):
    try:
        user = User.objects.get(username=request_user)
    except:
        return HttpResponse("User does not exists")
    
    if FollowerFollowing.objects.filter(user=user, following=request.user).exists():
        FollowerFollowing.objects.filter(user=user, following=request.user).update(accepted=True)
        FollowNotification.objects.filter(s_user=user, r_user=request.user).delete()
        return redirect("dashboard:profile", username=user.username)
    

#SECTION :          education

#NOTE :             add new education
@login_required
def education_add_view(request):
    if request.method == "POST":
        form = EducationForm(request.POST)

        if form.is_valid():
            Education.objects.create(
                user=request.user,
                school=form.cleaned_data["school"],
                degree=form.cleaned_data["degree"],
                start_date=form.cleaned_data["start_date"],
                end_date=form.cleaned_data["end_date"],
                grade=form.cleaned_data["grade"],
                description=form.cleaned_data["description"],
            )

            return redirect("dashboard:profile", username=request.user.username)
    else:
        form = EducationForm()
    
    context = {
        "form": form
    }

    return render(request=request, template_name="dashboard/education_add.html", context=context)


#NOTE :             edit education
@login_required
def education_edit_view(request, edu_id):
    try:
        education = Education.objects.get(pk=edu_id, user=request.user)
    except:
        return HttpResponse("Education not exists")
    
    if request.method == "POST":
        form = EducationForm(request.POST, instance=education)

        if form.is_valid():
            form.save()

            return redirect("dashboard:profile", username=request.user.username)
    else:
        form = EducationForm(instance=education)
    
    context = {
        "form": form
    }

    return render(request=request, template_name="dashboard/education_edit.html", context=context)


#NOTE :             delete education
@login_required
def education_delete_view(request, edu_id):
    try:
        education = Education.objects.get(pk=edu_id, user=request.user)
    except:
        return HttpResponse("Education not exists")
    
    education.delete()

    return redirect("dashboard:profile", username=request.user.username)



#SECTION :          Experience

#NOTE :             add new Experience
@login_required
def experience_add_view(request):
    if request.method == "POST":
        form = ExperienceForm(request.POST)

        if form.is_valid():
            Experience.objects.create(
                user=request.user,
                job_title=form.cleaned_data["job_title"],
                profile_title=form.cleaned_data["profile_title"],
                employment_type=form.cleaned_data["employment_type"],
                compnay_name=form.cleaned_data["compnay_name"],
                location=form.cleaned_data["location"],
                location_type=form.cleaned_data["location_type"],
                start_date=form.cleaned_data["start_date"],
                end_date=form.cleaned_data["end_date"],
                description=form.cleaned_data["description"],
            )

            return redirect("dashboard:profile", username=request.user.username)

    else:
        form = ExperienceForm()
    
    context = {
        "form": form
    }

    return render(request=request, template_name="dashboard/experience_add.html", context=context)


#NOTE :             edit Experience
@login_required
def experience_edit_view(request, exp_id):
    try:
        experience = Experience.objects.get(pk=exp_id, user=request.user)
    except:
        return HttpResponse("experience not exists")
    
    if request.method == "POST":
        form = ExperienceForm(request.POST, instance=experience)

        if form.is_valid():
            form.save()

            return redirect("dashboard:profile", username=request.user.username)
    else:
        form = ExperienceForm(instance=experience)
    
    context = {
        "form": form
    }

    return render(request=request, template_name="dashboard/experience_edit.html", context=context)


#NOTE :             delete Experience
@login_required
def experience_delete_view(request, exp_id):
    try:
        experience = Experience.objects.get(pk=exp_id, user=request.user)
    except:
        return HttpResponse("Experience not exists")
    
    experience.delete()

    return redirect("dashboard:profile", username=request.user.username)




#SECTION :          Project

#NOTE :             add new Project
@login_required
def project_add_view(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)

        if form.is_valid():
            Project.objects.create(
                user=request.user,
                title=form.cleaned_data["title"],
                link=form.cleaned_data["link"],
                description=form.cleaned_data["description"],
                start_date=form.cleaned_data["start_date"],
                end_date=form.cleaned_data["end_date"],
            )

            return redirect("dashboard:profile", username=request.user.username)
    else:
        form = ProjectForm()
    
    context = {
        "form": form
    }

    return render(request=request, template_name="dashboard/project_add.html", context=context)


#NOTE :             edit Project
@login_required
def project_edit_view(request, pro_id):
    try:
        project = Project.objects.get(pk=pro_id, user=request.user)
    except:
        return HttpResponse("project not exists")
    
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)

        if form.is_valid():
            form.save()

            return redirect("dashboard:profile", username=request.user.username)
    else:
        form = ProjectForm(instance=project)
    
    context = {
        "form": form
    }

    return render(request=request, template_name="dashboard/project_edit.html", context=context)


#NOTE :             delete Project
@login_required
def project_delete_view(request, pro_id):
    try:
        project = Project.objects.get(pk=pro_id, user=request.user)
    except:
        return HttpResponse("Project not exists")
    
    project.delete()

    return redirect("dashboard:profile", username=request.user.username)





#SECTION :          Skill

#NOTE :             add new Skill
@login_required
def skill_add_view(request):
    if request.method == "POST":
        form = SkillForm(request.POST)

        if form.is_valid():
            Skill.objects.create(
                user=request.user,
                skill=form.cleaned_data["skill"],
                skill_category=form.cleaned_data["skill_category"],
            )

            return redirect("dashboard:profile", username=request.user.username)
    else:
        form = SkillForm()
    
    context = {
        "form": form
    }

    return render(request=request, template_name="dashboard/skill_add.html", context=context)


#NOTE :             edit Skill
@login_required
def skill_edit_view(request, skill_id):
    try:
        skill = Skill.objects.get(pk=skill_id, user=request.user)
    except:
        return HttpResponse("Skill not exists")
    
    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)

        if form.is_valid():
            form.save()

            return redirect("dashboard:profile", username=request.user.username)
    else:
        form = SkillForm(instance=skill)
    
    context = {
        "form": form
    }

    return render(request=request, template_name="dashboard/skill_edit.html", context=context)


#NOTE :             delete Skill
@login_required
def skill_delete_view(request, skill_id):
    try:
        skill = Skill.objects.get(pk=skill_id, user=request.user)
    except:
        return HttpResponse("Skill not exists")
    
    skill.delete()

    return redirect("dashboard:profile", username=request.user.username)





#SECTION :          Language

#NOTE :             add new Language
@login_required
def language_add_view(request):
    if request.method == "POST":
        form = LanguageForm(request.POST)

        if form.is_valid():
            Language.objects.create(
                user=request.user,
                lang=form.cleaned_data["lang"],
            )

            return redirect("dashboard:profile", username=request.user.username)
    else:
        form = LanguageForm()
    
    context = {
        "form": form
    }

    return render(request=request, template_name="dashboard/language_add.html", context=context)


#NOTE :             edit language
@login_required
def language_edit_view(request, language_id):
    try:
        language = Language.objects.get(pk=language_id, user=request.user)
    except:
        return HttpResponse("language not exists")
    
    if request.method == "POST":
        form = LanguageForm(request.POST, instance=language)

        if form.is_valid():
            form.save()

            return redirect("dashboard:profile", username=request.user.username)
    else:
        form = LanguageForm(instance=language)
    
    context = {
        "form": form
    }

    return render(request=request, template_name="dashboard/language_edit.html", context=context)


#NOTE :             delete language
@login_required
def language_delete_view(request, language_id):
    try:
        language = Language.objects.get(pk=language_id, user=request.user)
    except:
        return HttpResponse("language not exists")
    
    language.delete()

    return redirect("dashboard:profile", username=request.user.username)







#SECTION :          profile view list
@login_required
def profile_view_list_view(request):
    profile_views = ProfileView.objects.filter(user=request.user).order_by("-visited_datetime")

    context = {
        "profile_views": profile_views
    }

    return render(request=request, template_name="dashboard/profile_view.html", context=context)



#SECTION :          upload resume

@login_required
def upload_resume_view(request):
    
    old_resume = None

    if ResumeFile.objects.filter(user=request.user).exists():
        #   update resume
        resume = ResumeFile.objects.get(user=request.user)

        old_resume = resume

        if request.method == "POST":
            form = ResumeFileForm(request.POST, request.FILES, instance=resume)

            if form.is_valid():
                
                ResumeFile.objects.update(
                    user=request.user,
                    resume=form.cleaned_data["resume"]
                )

                return redirect("dashboard:profile", username=request.user.username)
        else:
            form = ResumeFileForm(instance=resume)
    else:
        #       add resume
        if request.method == "POST":
            form = ResumeFileForm(request.POST, request.FILES)

            if form.is_valid():
                
                ResumeFile.objects.create(
                    user=request.user,
                    resume=form.cleaned_data["resume"]
                )

                return redirect("dashboard:profile", username=request.user.username)
        else:
            form = ResumeFileForm()

    context = {
        "form": form,
        "old_resume": old_resume
    }

    return render(request=request, template_name="dashboard/upload_resume.html", context=context)
    

#   your resume download and open / view link in new tab file only