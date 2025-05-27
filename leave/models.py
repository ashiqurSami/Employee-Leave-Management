from django.contrib.auth import get_user_model
from django.db import models
from accounts.models import Employee

# Create your models here.
class LeaveApplication(models.Model):
    LEAVE_TYPES=[
        ('Casual','Casual'),
        ('Sick','Sick'),
        ('Annual','Annual')
    ]
    STATUS=[
        ('Pending','Pending'),
        ('Approved','Approved'),
        ('Rejected','Rejected')
    ]

    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    leave_type=models.CharField(max_length=10,choices=LEAVE_TYPES)
    start_date=models.DateField()
    end_date=models.DateField()
    reason=models.TextField()
    status=models.CharField(max_length=10,choices=STATUS,default='Pending')
    approved_by=models.ForeignKey(get_user_model(),related_name='approved_leaves',null=True,blank=True,on_delete=models.SET_NULL)
    applied_on=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.user.username} - {self.leave_type}"