from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect, render
from .forms import EmployeeRegistrationForm
from .models import Employee

def register_view(request):
    if request.method=="POST":
        form= EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            Employee.objects.create()
            login(request,user)
            return redirect('login')
    else:
        form=EmployeeRegistrationForm()
    return render(request,'accounts/register.html',{'form':form})