import uuid

from django.db import models
from django.contrib.auth.models import User

from dashboard.models import ResumeFile





#SECTION :              Page
class Page(models.Model):
    ORGANIZATION_SIZE_CHOICE = {
        "0-1": "0-1",
        "1-10": "2-10",
        "11-50": "11-50",
        "51-200": "51-200",
        "201-500": "201-500",
        "501-1000": "501-1000",
        "1001-5000": "1001-5000",
        "5001-10000": "5001-10000",
        "10000+": "10000+",
    }

    INDUSTRY_TYPE_CHOICE = {
        "Real State": "Real State",
        "Automotive": "Automotive",
        "Financial Services": "Financial Services",
        "Healthcare": "Healthcare",
        "E-commerce": "E-commerce",
        "Retail": "Retail",
        "Technology": "Technology",
        "Gambling": "Gambling",
        "Agriculture": "Agriculture",
        "Transport": "Transport",
    }

    ORGANIZATION_TYPE_CHOICE = {
        "Public Company": "Public Company",
        "Self-employed": "Self-employed",
        "Government agency": "Government agency",
        "Non-profit": "Non-profit",
        "Sole proprietorship": "Sole proprietorship",
        "Privately held": "Privately held",
        "Partnership": "Partnership"
    }

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="page_user")
    logo = models.ImageField(upload_to="pages/logo/", default="page_logo.jpg")
    cover_image = models.ImageField(upload_to="pages/cover/", default="page_cover.jpg")
    name = models.CharField(max_length=50, unique=True)
    headline = models.CharField(max_length=200, null=True, blank=True)
    website = models.URLField(max_length=150)
    industry = models.CharField(max_length=100, choices=INDUSTRY_TYPE_CHOICE)
    organization_size = models.CharField(max_length=20, choices=ORGANIZATION_SIZE_CHOICE)
    organization_type = models.CharField(max_length=100, choices=ORGANIZATION_TYPE_CHOICE)
    description = models.TextField(max_length=2000)

    contact_number = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=200)
    address = models.CharField(max_length=250)
    year_founded = models.DateField()

    unique_id = models.UUIDField(default=uuid.uuid4)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


#SECTION :              Page Follower
class PageFollower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="page_follower_user")
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="page_following")
    created_date = models.DateTimeField(auto_now_add=True)
    unique_id = models.UUIDField(default=uuid.uuid4)


#SECTION :              Job
class Job(models.Model):
    JOB_LOCATION_TYPE_CHOICE = {
        "On-site": "On-site",
        "Remote": "Remote",
        "Hybrid": "Hybrid",
    }

    EMPLOYMENT_TYPE_CHOICE = {
        "Full-time": "Full-time",
        "Part-time": "Part-time",
        "Temporary": "Temporary",
        "Contract": "Contract",
    }

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="job_post_user")
    company = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="job_post_company")

    job_title = models.CharField(max_length=200)
    about_job = models.TextField(max_length=1000)
    skills = models.CharField(max_length=300)
    qualifications = models.TextField(max_length=500)
    responsibilities = models.TextField(max_length=500)

    job_location_type = models.CharField(max_length=100, choices=JOB_LOCATION_TYPE_CHOICE)
    employment_type = models.CharField(max_length=100, choices=EMPLOYMENT_TYPE_CHOICE)
    till_apply = models.DateField()
    
    unique_id = models.UUIDField(default=uuid.uuid4)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.job_title


#SECTION :              Applied Job
class AppliedJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applied_job_user")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applied_job")
    applied_date = models.DateTimeField(auto_now_add=True)
    unique_id = models.UUIDField(default=uuid.uuid4)

    def get_resume(self):
        resume_obj = ResumeFile.objects.get(user=self.user)
        resume = resume_obj.resume
        return resume


#SECTION :              Saved Job
class SavedJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="saved_job_user")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="saved_job")
    saved_date = models.DateTimeField(auto_now_add=True)
    unique_id = models.UUIDField(default=uuid.uuid4)