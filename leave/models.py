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
    applied_on=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.user.username} - {self.leave_type}"