from django import forms

from company.models import Page, Job




#SECTION :          page form
class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ["name", "headline", "logo", "cover_image", "website", "industry", "organization_size", "organization_type", "contact_number", "email_address", "address", "year_founded", "description"]

        widgets = {
            "name": forms.TextInput(attrs=({"class": "form-control mb-3"})),
            "headline": forms.TextInput(attrs=({"class": "form-control mb-3"})),
            "logo": forms.FileInput(attrs=({"class": "form-control  mb-3"})),
            "cover_image": forms.FileInput(attrs=({"class": "form-control  mb-3"})),
            "website": forms.URLInput(attrs=({"class": "form-control  mb-3"})),
            "industry": forms.Select(attrs=({"class": "form-control  mb-3"})),
            "organization_size": forms.Select(attrs=({"class": "form-control  mb-3"})),
            "organization_type": forms.Select(attrs=({"class": "form-control  mb-3"})),
            "description": forms.Textarea(attrs=({"class": "form-control  mb-3", "rows": 3})),
            "contact_number": forms.TextInput(attrs=({"class": "form-control  mb-3"})),
            "email_address": forms.EmailInput(attrs=({"class": "form-control  mb-3"})),
            "address": forms.TextInput(attrs=({"class": "form-control  mb-3"})),
            "year_founded": forms.DateInput(attrs=({"class": "form-control  mb-3"}))
        }

#SECTION :          job form
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["job_title", "skills", "job_location_type", "employment_type", "till_apply", "qualifications", "responsibilities", "about_job"]

        widgets = {
            "job_title": forms.TextInput(attrs=({"class": "form-control mb-3"})),
            "skills": forms.TextInput(attrs=({"class": "form-control mb-3"})),
            "about_job": forms.Textarea(attrs=({"class": "form-control mb-3", "rows": 3})),
            "qualifications": forms.Textarea(attrs=({"class": "form-control mb-3", "rows": 3})),
            "responsibilities": forms.Textarea(attrs=({"class": "form-control mb-3", "rows": 3})),
            "job_location_type": forms.Select(attrs=({"class": "form-control mb-3"})),
            "employment_type": forms.Select(attrs=({"class": "form-control mb-3"})),
            "till_apply": forms.DateInput(attrs=({"class": "form-control mb-3", "type": "date"}))
        }