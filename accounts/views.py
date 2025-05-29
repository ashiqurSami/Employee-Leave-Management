from django.contrib.auth.decorators import login_required, login_not_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect, render
from .forms import EmployeeRegistrationForm,EmployeeProfileForm
from .models import Employee
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method=="POST":
        form= EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            Employee.objects.create(user=user)
            login(request,user)
            return redirect('profile')
    else:
        form=EmployeeRegistrationForm()
    return render(request,'accounts/register.html',{'form':form})

@login_required
def profile_view(request):
    employee,_=Employee.objects.get_or_create(user=request.user)
    if request.method=="POST":
        form=EmployeeProfileForm(request.POST,request.FILES,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('profile')
    else:
        form=EmployeeProfileForm(instance=employee)
    return render(request,'accounts/profile.html',{'form':form})

@login_required
def login_redirect_view(request):
    if request.user.is_staff:
        return redirect('/leave/admin-dashboard/')
    else:
        return redirect('/leave/my-leaves/')