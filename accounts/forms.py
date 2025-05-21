from django import forms
from .models import Employee
from django.contrib.auth.models import User

class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['department', 'job_title', 'profile_photo']
        widgets = {
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

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