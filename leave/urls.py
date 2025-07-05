from django.urls import path
from leave import views


urlpatterns = [
    path('apply/',views.apply_leave, name='apply_leave'),
    path('my-leaves/', views.leave_list, name='leave_list'),
    path('admin/',views.admin_leave_list, name='admin_leave_list'),
    path('approve/<int:leave_id>/', views.approve_leave, name='approve_leave'),
    path('reject/<int:leave_id>/', views.reject_leave, name='reject_leave'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]