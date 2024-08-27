from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

from dashboard.models import Profile, Education, Experience, Project, Skill, Language, ResumeFile


#SECTION :          Profile Edit

#NOTE :             build in profile edit
class AEditProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email Address",
        }

        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control mb-3"}),
            "last_name": forms.TextInput(attrs={"class": "form-control mb-3"}),
            "email": forms.EmailInput(attrs={"class": "form-control mb-3"}),
        }


#NOTE :             custom profile edit
class BEditProfileForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ["headline", "website", "city", "state", "country", "profile_image", "contact_number", "dob", "gender", "account_type", "bio"]

        widgets = {
            "headline": forms.TextInput(attrs={"class": "form-control mb-3"}),
            "city": forms.TextInput(attrs={"class": "form-control mb-3"}),
            "state": forms.TextInput(attrs={"class": "form-control mb-3"}),
            "country": forms.TextInput(attrs={"class": "form-control mb-3"}),
            "profile_image": forms.FileInput(attrs={"class": "form-control mb-3"}),
            "website": forms.TextInput(attrs={"class": "form-control mb-3"}),
            "dob": forms.DateInput(attrs={"class": "form-control mb-3"}),
            "contact_number": forms.TextInput(attrs={"class": "form-control mb-3"}),
            "bio": forms.Textarea(attrs={"class": "form-control mb-3"}),
            "gender": forms.Select(attrs={"class": "form-control mb-3"}),
            "account_type": forms.Select(attrs={"class": "form-control mb-3"}),
        }


#SECTION :          education form
class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ["school", "degree", "start_date", "end_date", "grade", "description"]

        widgets = {
            "school": forms.TextInput(attrs={"class": "form-control mb-3"}),
            "degree": forms.TextInput(attrs={"class": "form-control mb-3"}),
            "start_date": forms.DateInput(attrs={"class": "form-control mb-3"}),
            "end_date": forms.DateInput(attrs={"class": "form-control mb-3"}),
            "grade": forms.TextInput(attrs={"class": "form-control mb-3"}),
            "description": forms.Textarea(attrs={"class": "form-control mb-3", "rows":4}),
        }


#SECTION :          Experience
class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ["job_title", "profile_title", "compnay_name", "employment_type", "location", "location_type", "start_date", "end_date", "description"]

        widgets = {
            "school": forms.TextInput(attrs={"class": "form-control mb-3"}),
            "job_title": forms.TextInput(attrs={"class": "form-control mb-3"}),
            "profile_title": forms.TextInput(attrs={"class": "form-control mb-3"}),
            "employment_type": forms.Select(attrs={"class": "form-control mb-3"}),
            "compnay_name": forms.TextInput(attrs={"class": "form-control mb-3"}),
            "location": forms.TextInput(attrs={"class": "form-control mb-3"}),
            "location_type": forms.Select(attrs={"class": "form-control mb-3"}),
            "start_date": forms.DateInput(attrs={"class": "form-control mb-3"}),
            "end_date": forms.DateInput(attrs={"class": "form-control mb-3"}),
            "description": forms.Textarea(attrs={"class": "form-control mb-3", "rows": 4}),
        }


#SECTION :          Project
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "link", "description", "start_date", "end_date"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control mb-3"}),
            "link": forms.URLInput(attrs={"class": "form-control mb-3"}),
            "description": forms.Textarea(attrs={"class": "form-control mb-3", "rows": 4}),
            "start_date": forms.DateInput(attrs={"class": "form-control mb-3"}),
            "end_date": forms.DateInput(attrs={"class": "form-control mb-3"}),
        }


#SECTION :          Skill
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ["skill", "skill_category"]

        widgets = {
            "skill": forms.TextInput(attrs={"class": "form-control mb-3"}),
            "skill_category": forms.Select(attrs={"class": "form-control mb-3"}),
        }


#SECTION :          Language
class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ["lang"]

        widgets = {
            "lang": forms.Select(attrs={"class": "form-control mb-3"}),
        }


#SECTION :          resume form
class ResumeFileForm(forms.ModelForm):
    class Meta:
        model = ResumeFile
        fields = ["resume", ]

        widgets = {
            "resume": forms.FileInput(attrs={"class": "form-control mb-3"}),
        }