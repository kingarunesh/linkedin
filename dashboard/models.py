from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

import uuid
import os


#NOTE :         resume validation
def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError(f'Unsupported file extension. Please upload valid file with these extensions: {valid_extensions}')
    


#SECTION :     Profile
class Profile(models.Model):
    GENDER_CHOICE = {
        "Male": "Male",
        "Female": "Female",
        "Other": "Other"
    }

    ACCOUNT_TYPE_CHOICE = {
        "Public": "Public",
        "Private": "Private",
    }

    USER_TYPE_CHOICE = {
        "user": "user",
        "recruiter": "recruiter",
    }


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    headline = models.CharField(max_length=50, blank=True, null=True)

    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    state = models.CharField(max_length=250, null=True, blank=True)
    country = models.CharField(max_length=250, null=True, blank=True)
    profile_image = models.ImageField(upload_to=f"users/profile/", null=True, blank=True, default="profile.png")
    website = models.URLField(null=True, blank=True, max_length=100)
    bio = models.TextField(max_length=500, null=True, blank=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICE, default="Private")
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    unique_id = models.UUIDField(default=uuid.uuid4)
    verify = models.BooleanField(default=False, null=True, blank=True)


#SECTION:       verify account


#SECTION :     Skills
class Skill(models.Model):
    SKILL_CATEGORY_CHOICE = {
        "Programming Languages": "Programming Languages",
        "Framework": "Framework",
        "Library": "Library",
        "Module": "Module",
        "Other": "Other",
    }
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=50)
    skill_category = models.CharField(max_length=30, choices=SKILL_CATEGORY_CHOICE)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    unique_id = models.UUIDField(default=uuid.uuid4, null=True, blank=True)


#SECTION :     Education
class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.CharField(max_length=250)
    degree = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    grade = models.FloatField()
    description = models.TextField(max_length=150)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    unique_id = models.UUIDField(default=uuid.uuid4, null=True, blank=True)


#SECTION :         Experience
class Experience(models.Model):
    EMPLOYMENT_TYPE_CHOICE = {
        "Full Time": "Full Time",
        "Part Time": "Part Time",
        "Internship": "Internship",
        "Self Employed": "Self Employed",
        "Freelance": "Freelance",
        "Trainee": "Trainee"
    }

    LOCATION_TYPE_CHOICE = {
        "On-site": "On-site",
        "remote": "Remote",
        "Hybrid": "Hybrid"
    }
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=250)
    profile_title = models.CharField(max_length=250)
    employment_type = models.CharField(max_length=50, choices=EMPLOYMENT_TYPE_CHOICE)
    compnay_name = models.CharField(max_length=150)
    location = models.CharField(max_length=250)
    location_type = models.CharField(max_length=250, choices=LOCATION_TYPE_CHOICE)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(max_length=150)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    unique_id = models.UUIDField(default=uuid.uuid4, null=True, blank=True)


#SECTION :         Project
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    link = models.URLField(null=True, blank=True)
    description = models.TextField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    unique_id = models.UUIDField(default=uuid.uuid4, null=True, blank=True)


#SECTION :         user profile view history
class ProfileView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="current_user")
    visited_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="visited_user")
    visited_datetime = models.DateTimeField(auto_now_add=True)
    unique_id = models.UUIDField(default=uuid.uuid4, null=True, blank=True)



#SECTION :         follower & following
class FollowerFollowing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", null=True)
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following", null=True)
    accepted = models.BooleanField(default=False, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    unique_id = models.UUIDField(default=uuid.uuid4, null=True, blank=True)

    # def __str__(self):
    #     return f"{self.user} - {self.following.username}"



#SECTION :         languages
class Language(models.Model):
    LANG_CHOICE = {
        "English": "English",
        "Hindi": "Hindi",
        "Odia": "Odia",
        "Bengali": "Bengali",
        "Marathi": "Marathi",
        "Telugu": "Telugu",
        "Tamil": "Tamil",
        "Gujarati": "Gujarati",
        "Urdu": "Urdu",
        "Kannada": "Kannada",
        "Malayalam": "Malayalam",
    }

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lang = models.CharField(max_length=30, default="English", choices=LANG_CHOICE)
    unique_id = models.UUIDField(default=uuid.uuid4, null=True, blank=True)


#SECTION :          Block User
class BlockUser(models.Model):
    blocker_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blocker_user")
    blocked_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blocked_user")
    block_date = models.DateTimeField(auto_now_add=True)
    unique_id = models.UUIDField(default=uuid.uuid4, null=True, blank=True)



#SECTION :              resume upload
class ResumeFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="resume_user")
    resume = models.FileField(upload_to="users/resume/", validators=[validate_file_extension])
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    unique_id = models.UUIDField(default=uuid.uuid4)

    def filename(self):
        return os.path.basename(self.resume.name)