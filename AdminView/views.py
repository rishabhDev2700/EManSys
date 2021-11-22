from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from AdminView.forms import UserRegistrationForm, UserUpdateForm, DepartmentForm, PayGradeForm
from Authentication.models import User, Department, PayGrade


def get_dashboard(request):
    users = User.objects.filter(is_admin=False)
    departments = Department.objects.all()
    pay_grades = PayGrade.objects.all()
    print(users)
    return render(request, 'admin_view/dashboard.html', {'users': users,'departments':departments,'pay_grades':pay_grades})


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('dashboard')
    form = UserRegistrationForm()
    return render(request, 'admin_view/user_form.html', {'form': form})


def update_user(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return HttpResponse("There was some problem please try again!")
    form = UserUpdateForm(instance=request.user)
    return render(request, 'admin_view/user_form.html', {'form': form})


def delete_user(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect('dashboard')


def get_departments(request):
    departments = Department.objects.all()
    return render(request, 'admin_view/departments.html', {'departments': departments})


def get_pay_grades(request):
    pay_grades = PayGrade.objects.all()
    return render(request, 'admin_view/pay_grades.html', {'pay_grades': pay_grades})


def department_form(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return HttpResponse("Error Occurred")
    form = DepartmentForm()
    return render(request, 'admin_view/department_form.html', {'form': form})


def pay_grade_form(request):
    if request.method == 'POST':
        form = PayGradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return HttpResponse("Error Occurred")
    form = PayGradeForm()
    return render(request, "admin_view/pay_form.html", {"form": form})


def delete_department(request, id):
    department = Department.objects.get(pk=id)
    department.delete()
    return redirect('departments')


def delete_pay_grade(request, id):
    pay_grade = PayGrade.objects.get(pk=id)
    pay_grade.delete()
    return redirect('pay_grades')
