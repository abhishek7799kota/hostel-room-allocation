from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('apply/', views.apply_hostel, name='apply'),
    path('success/', views.success, name='success'),
    path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'),
    path('add-student/', views.add_student, name='add-student'),
    path('add-room/', views.add_room, name='add-room'),
    path('logout/', views.logout_view, name='logout'),
]
