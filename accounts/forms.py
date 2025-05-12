from django import forms
from .models import Employee
from django.contrib.auth.models import User

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['department', 'job_title', 'profile_photo']

class EmployeeRegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields=['username','email','password']

    def clean(self):
        cleaned_data=super().clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data