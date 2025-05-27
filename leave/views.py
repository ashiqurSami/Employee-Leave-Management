from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render, get_object_or_404
from accounts.models import Employee
from leave.forms import LeaveApplicationForm
from .models import LeaveApplication

def is_admin(user):
    return   user.is_superuser or user.is_staff

@login_required(login_url='login')
def apply_leave(request):
    employee=Employee.objects.get(user=request.user)
    if request.method == 'POST':
        form = LeaveApplicationForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.employee = employee
            leave.save()
            return redirect('login')
    else:
        form = LeaveApplicationForm()
    return render(request, 'leave/apply_leave.html', {'form': form})

@login_required(login_url='login')
def leave_list(request):
    employee = Employee.objects.get(user=request.user)
    leaves = LeaveApplication.objects.filter(employee=employee)
    return render(request, 'leave/leave_list.html', {'leaves': leaves})

@login_required(login_url='login')
@user_passes_test(is_admin)
def approve_leave(request, leave_id):
    leave=get_object_or_404(LeaveApplication,id=leave_id)
    leave.status= 'Approved'
    leave.approved_by=request.user
    leave.save()
    return redirect('admin_leave_list')

@login_required(login_url='login')
@user_passes_test(is_admin)
def reject_leave(request,leave_id):
    leave=get_object_or_404(LeaveApplication,id=leave_id)
    leave.status= 'Rejected'
    leave.approved_by=request.user
    leave.save()
    return redirect('admin_leave_list')

@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_leave_list(request):
    leaves = LeaveApplication.objects.all().order_by('-applied_on')
    return render(request, 'leave/admin_leave_list.html', {'leaves': leaves})

