from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    # path('register/student/', views.register_student, name='register_student'),
    # path('register/department/', views.register_department, name='register_department'),
    # path('register/recruiter/', views.register_recruiter, name='register_recruiter'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
    path('dashboard/department/', views.department_dashboard, name='department_dashboard'),
    path('dashboard/recruiter/', views.recruiter_dashboard, name='recruiter_dashboard'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('profile/admin/', views.admin_profile, name='admin_profile'),
    path('users/admin/', views.admin_users, name='admin_users'),
    path('products/admin/', views.admin_products, name='admin_products'),
    path('profile/department/', views.department_profile, name='department_profile'),
    path('products/department/', views.department_products, name='department_products'),
    path('edit-products/department/', views.edit_products, name='edit_products'),
    path('add-products/department/', views.add_products, name='add_products'),
    path('delete-products/department/', views.delete_products, name='delete_products'),
]
