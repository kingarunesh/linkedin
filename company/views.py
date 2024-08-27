from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from dashboard.models import Profile

from company.forms import PageForm, JobForm
from company.models import Page, Job, AppliedJob, SavedJob, PageFollower
from dashboard.models import ResumeFile
from django.contrib import messages



#SECTION :          page
#NOTE :     list page
@login_required
def page_list_view(request):
    #NOTE :     perosnal page list
    pages = Page.objects.filter(user=request.user).order_by("-last_updated")

    #NOTE :     all page list
    all_pages = Page.objects.all().order_by("-last_updated")

    context = {
        "pages": pages,
        "all_pages": all_pages
    }

    return render(request=request, template_name="company/page_list.html", context=context)



#NOTE :      create page
@login_required
def create_page_view(request):

    #   user account must be verify by register email address
    if not Profile.objects.get(user=request.user).verify:
        return render(request=request, template_name="error/404.html", context={"message": "You must verify your register email, then you can create 'Page'"})

    if request.method == "POST":
        form = PageForm(request.POST, request.FILES)

        if form.is_valid():
            page = Page.objects.create(
                user=request.user,
                logo=form.cleaned_data["logo"],
                cover_image=form.cleaned_data["cover_image"],
                name=form.cleaned_data["name"],
                website=form.cleaned_data["website"],
                industry=form.cleaned_data["industry"],
                organization_size=form.cleaned_data["organization_size"],
                organization_type=form.cleaned_data["organization_type"],
                description=form.cleaned_data["description"],
                contact_number=form.cleaned_data["contact_number"],
                email_address=form.cleaned_data["email_address"],
                address=form.cleaned_data["address"],
                year_founded=form.cleaned_data["year_founded"],
            )

            return redirect("company:detail_page", page_id=page.id)
    else:
        form = PageForm()

    context = {
        "form": form
    }
    
    return render(request=request, template_name="company/create_page.html", context=context)



#NOTE :      page details
@login_required
def detail_page_view(request, page_id):
    try:
        page = Page.objects.get(pk=page_id)
    except:
        return render(request=request, template_name="error/404.html", context={"message": "Page does not exists."})
    
    page_follow = PageFollower.objects.filter(user=request.user, page=page).exists()

    total_page_follower = PageFollower.objects.filter(page=page).count()


    context = {
        "page": page,
        "page_follow": page_follow,
        "total_page_follower": total_page_follower
    }

    return render(request=request, template_name="company/detail_page.html", context=context)


#NOTE :      edit page
@login_required
def edit_page_view(request, page_id):
    #NOTE :         page exists or not
    try:
        page = Page.objects.get(pk=page_id)
    except:
        return render(request=request, template_name="error/404.html", context={"message": "Page does not exists."})
    
    #NOTE :         created page user can only edit page
    if page.user != request.user:
        return render(request=request, template_name="error/404.html", context={"message": "Page does not exists."})
    
    #NOTE :         edit page
    if request.method == "POST":
        form = PageForm(request.POST, request.FILES, instance=page)

        if form.is_valid():
            form.save()
            return redirect("company:detail_page", page_id=page.id)
    else:
        form = PageForm(instance=page)
    
    context = {
        "form": form
    }

    return render(request=request, template_name="company/edit_page.html", context=context)


#NOTE :          delete page
@login_required
def delete_page_view(request, page_id):
    #NOTE :         page exists or not
    try:
        page = Page.objects.get(pk=page_id)
    except:
        return render(request=request, template_name="error/404.html", context={"message": "Page does not exists."})
    
    #NOTE :         created page user can only edit page
    if page.user != request.user:
        return render(request=request, template_name="error/404.html", context={"message": "Page does not exists."})
    
    #NOTE :         delete page
    page.delete()
    return redirect("home:home")


#NOTE :         follower page
@login_required
def follow_page_view(request, page_id):
    try:
        page = Page.objects.get(pk=page_id)
    except:
        return render(request=request, template_name="error/404.html", context={"message": "Page does not exists."})
    
    if PageFollower.objects.filter(user=request.user, page=page).exists():
        PageFollower.objects.filter(user=request.user, page=page).delete()
    else:
        PageFollower.objects.create(user=request.user, page=page)
    
    return redirect("company:detail_page", page_id=page_id)


#NOTE :     follow page list
@login_required
def follow_page_list_view(request):
    page_follow_list = PageFollower.objects.filter(user=request.user).order_by("-created_date")

    context = {
        "page_follow_list": page_follow_list
    }

    return render(request=request, template_name="company/follow_page_list.html", context=context)


#SECTION:           job
#NOTE :      job post
@login_required
def create_job_view(request, page_id):

    try:
        company = Page.objects.get(pk=page_id, user=request.user)
    except:
        return render(request=request, template_name="error/404.html", context={"message": "Page does not exists."})

    if request.method == "POST":
        form = JobForm(request.POST)

        if form.is_valid():
            Job.objects.create(
                user=request.user,
                company=company,
                job_title=form.cleaned_data["job_title"],
                about_job=form.cleaned_data["about_job"],
                skills=form.cleaned_data["skills"],
                qualifications=form.cleaned_data["qualifications"],
                responsibilities=form.cleaned_data["responsibilities"],
                job_location_type=form.cleaned_data["job_location_type"],
                employment_type=form.cleaned_data["employment_type"],
                till_apply=form.cleaned_data["till_apply"],
            )

        
    else:
        form = JobForm()

    context = {
        "form": form
    }
    
    return render(request=request, template_name="company/create_job.html", context=context)



#NOTE :      job list
@login_required
def list_job_view(request):
    jobs = Job.objects.filter(user=request.user).order_by("-last_updated")

    all_jobs = Job.objects.all().order_by("-last_updated")

    context = {
        "jobs": jobs,
        "all_jobs": all_jobs
    }
    
    return render(request=request, template_name="company/list_job.html", context=context)


#NOTE :      detail job
@login_required
def detail_job_view(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
    except:
        return render(request=request, template_name="error/404.html", context={"message": "Page does not exists."})
    
    apply_job = False
    if AppliedJob.objects.filter(user=request.user, job=job).exists():
        apply_job = True
    
    #!      saved job
    saved_job = False
    if SavedJob.objects.filter(user=request.user, job=job).exists():
        saved_job = True
    
    context = {
        "job": job,
        "apply_job": apply_job,
        "saved_job": saved_job
    }

    return render(request=request, template_name="company/detail_job.html", context=context)


#NOTE :          edit job
@login_required
def edit_job_view(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
    except:
        return render(request=request, template_name="error/404.html", context={"message": "Page does not exists."})
    
    if request.user != job.user:
        return render(request=request, template_name="error/404.html", context={"message": "Page does not exists."})
    

    if request.method == "POST":
        form = JobForm(request.POST, instance=job)

        if form.is_valid():
            form.save()

            return redirect("company:detail_job", job_id=job.id)
    else:
        form = JobForm(instance=job)

    context = {
        "form": form,
        "job": job
    }

    return render(request=request, template_name="company/edit_job.html", context=context)


#NOTE :          delete job
@login_required
def delete_job_view(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
    except:
        return render(request=request, template_name="error/404.html", context={"message": "Page does not exists."})
    
    if request.user != job.user:
        return render(request=request, template_name="error/404.html", context={"message": "Page does not exists."})
    
    job.delete()

    return redirect("company:list_job")



#NOTE :      apply for job

#NOTE :         apply job
@login_required
def apply_job_view(request, job_id):
    #!      if current_user have not uploaded reusme
    if not ResumeFile.objects.filter(user=request.user).exists():
        messages.error(request=request, message="Please upload resume to apply before any job.")
        return redirect("dashboard:upload_resume")

    try:
        job = Job.objects.get(pk=job_id)
    except:
        return render(request=request, template_name="error/404.html", context={"message": "Page does not exists."})

    #   if current_user already apply for job display applied button not apply
    if AppliedJob.objects.filter(user=request.user, job=job).exists():
        AppliedJob.objects.filter(user=request.user, job=job).delete()
    else:
        AppliedJob.objects.create(user=request.user, job=job)
 
    return redirect("company:detail_job", job_id=job.id)


#NOTE :     applied job list only for job posted user
@login_required
def applied_your_job_list_view(request):
    #   current login user if have posted any job then display list

    #!      job = field in AppliedJob | __ = means filter | user = job user
    your_job_applied = AppliedJob.objects.filter(job__user=request.user).order_by("-applied_date")

    applied_jobs = AppliedJob.objects.filter(user=request.user).order_by("-applied_date")

    context = {
        "your_job_applied": your_job_applied,
        "applied_jobs": applied_jobs
    }

    return render(request=request, template_name="company/applied_your_job_list.html", context=context)


#NOTE :         save(bookmark) job
@login_required
def save_job_view(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
    except:
        return render(request=request, template_name="error/404.html", context={"message": "Page does not exists."})
    
    if SavedJob.objects.filter(user=request.user, job=job).exists():
        SavedJob.objects.filter(user=request.user, job=job).delete()
    else:
        SavedJob.objects.create(user=request.user, job=job)
    
    return redirect("company:detail_job", job_id=job_id)


#NOTE :         saved(bookmark) job
@login_required
def saved_job_list_view(request):
    
    saved_jobs_list = SavedJob.objects.filter(user=request.user).order_by("-saved_date")
    
    context = {
        "saved_jobs_list": saved_jobs_list
    }

    return render(request=request, template_name="company/saved_jobs_list.html", context=context)