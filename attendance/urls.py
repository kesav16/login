from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.login_view, name='login_view'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('check-in/', views.check_in, name='check_in'),
    path('check-out/', views.check_out, name='check_out'),
    path('apply-leave/', views.apply_leave, name='apply_leave'),
    path("generate-qr/",views.generate_qr, name="generate_qr"),    
    path('profile/', views.profile_view, name='profile'),
    path('admin_profile/', views.admin_profile_view, name='admin_profile'),
    path('admin-dashboard/', views.admin_dashboard, name="admin_dashboard"),
    path('leave-management/', views.leave_management, name='leave_management'),
    path('leave-status/', views.leave_status, name='leave_status'),
    path('approve-leave/<int:leave_id>/',views. approve_leave, name='approve_leave'),
    path('reject-leave/<int:leave_id>/',views. reject_leave, name='reject_leave'),
    path('manage-employees/', views.manage_employees, name='manage_employees'),
    path('view-attendance/', views.view_attendance, name='view_attendance'),
    path('select-employee/', views.select_employee, name='select_employee'),
    path('download-attendance/<str:employee_id>/',views. download_employee_attendance, name='download_employee_attendance'),
    path('payroll/generate/', views.generate_payslip, name='generate_payroll'),
    path('payroll/list/',views. payroll_list, name='payroll_list'),
    path('payroll/download-csv/', views.download_payroll_csv, name='download_payroll_csv'),
      path('payroll/fetch-details/<int:employee_id>/', views.fetch_employee_details, name='fetch_employee_details'),
      path('payroll/payslip/<int:payroll_id>/',views. generate_payslip, name='generate_payslip_pdf'),
      path('break-in/', views.break_in, name='break_in'),
    path('break-out/',views. break_out, name='break_out'),
   
]

    


