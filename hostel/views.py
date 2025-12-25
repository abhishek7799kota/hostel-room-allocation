from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from datetime import datetime
from .models import Student, Room, Allocation


def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'hostel/login.html')


def register(request):
    if request.method == "POST":
        user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        Student.objects.create(
            user=user,
            roll_no=request.POST['roll_no'],
            department=request.POST['department'],
            year=request.POST['year']
        )
        login(request, user)
        return redirect('dashboard')
    return render(request, 'hostel/register.html')


from datetime import datetime

@login_required
def dashboard(request):
    student, created = Student.objects.get_or_create(
        user=request.user,
        defaults={
            'roll_no': 'TEMP',
            'department': 'TEMP',
            'year': 1
        }
    )

    allocation = Allocation.objects.filter(student=student).first()

    hour = datetime.now().hour
    if hour < 12:
        greeting = "Good Morning"
    elif hour < 17:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    return render(request, 'hostel/dashboard.html', {
        'allocation': allocation,
        'greeting': greeting
    })



@login_required
def apply_hostel(request):
    student = Student.objects.get(user=request.user)
    if request.method == "POST":
        for room in Room.objects.all():
            if room.is_available():
                Allocation.objects.create(student=student, room=room)
                room.occupied += 1
                room.save()
                return redirect('success')
        return render(request, 'hostel/no_rooms.html')
    return render(request, 'hostel/apply.html')


@login_required
def success(request):
    return render(request, 'hostel/success.html')


@staff_member_required
def admin_dashboard(request):
    return render(request, 'hostel/admin_dashboard.html')


@staff_member_required
def add_student(request):
    if request.method == "POST":
        user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        Student.objects.create(
            user=user,
            roll_no=request.POST['roll_no'],
            department=request.POST['department'],
            year=request.POST['year']
        )
        return redirect('admin-dashboard')
    return render(request, 'hostel/add_student.html')


@staff_member_required
def add_room(request):
    if request.method == "POST":
        Room.objects.create(
            room_number=request.POST['room_number'],
            capacity=request.POST['capacity']
        )
        return redirect('admin-dashboard')
    return render(request, 'hostel/add_room.html')


def logout_view(request):
    logout(request)
    return redirect('login')
