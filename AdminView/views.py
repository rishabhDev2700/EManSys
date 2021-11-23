from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, redirect
from AdminView.decorators import check_if_admin
from AdminView.forms import UserRegistrationForm, UserUpdateForm, DepartmentForm, PayGradeForm
from Authentication.models import User, Department, PayGrade


# Create your views here.


@login_required(login_url='login')
@user_passes_test(check_if_admin)
def get_dashboard(request):
    users = User.objects.filter(is_admin=False)
    departments = Department.objects.all()
    pay_grades = PayGrade.objects.all()
    print(users)
    return render(request, 'admin_view/dashboard.html',
                  {'users': users, 'departments': departments, 'pay_grades': pay_grades})


@login_required(login_url='login')
@user_passes_test(check_if_admin)
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    form = UserRegistrationForm()
    return render(request, 'admin_view/user_form.html', {'form': form})


@login_required(login_url='login')
@user_passes_test(check_if_admin)
def update_user(request, pk):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=User.objects.get(pk=pk))
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return HttpResponse("There was some problem please try again!")
    user = User.objects.get(pk=pk)
    form = UserUpdateForm(instance=user)
    return render(request, 'admin_view/user_form.html', {'form': form})


@login_required(login_url='login')
@user_passes_test(check_if_admin)
def delete_user(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect('dashboard')


@login_required(login_url='login')
@user_passes_test(check_if_admin)
def get_departments(request):
    departments = Department.objects.all()
    return render(request, 'admin_view/departments.html', {'departments': departments})


@login_required(login_url='login')
@user_passes_test(check_if_admin)
def get_pay_grades(request):
    pay_grades = PayGrade.objects.all()
    return render(request, 'admin_view/pay_grades.html', {'pay_grades': pay_grades})


@login_required(login_url='login')
@user_passes_test(check_if_admin)
def department_form(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('departments')
        else:
            return HttpResponse("Error Occurred")
    form = DepartmentForm()
    return render(request, 'admin_view/department_form.html', {'form': form})


@login_required(login_url='login')
@user_passes_test(check_if_admin)
def department_update_form(request, pk):
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=Department.objects.get(pk=pk))
        if form.is_valid():
            form.save()
            return redirect('departments')
        else:
            return HttpResponse("Error Occurred")
    department = Department.objects.get(pk=pk)
    form = DepartmentForm(instance=department)
    return render(request, 'admin_view/department_form.html', {'form': form})


@login_required(login_url='login')
@user_passes_test(check_if_admin)
def pay_grade_form(request):
    if request.method == 'POST':
        form = PayGradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pay_grades')
        else:
            return HttpResponse("Error Occurred")
    form = PayGradeForm()
    return render(request, "admin_view/pay_form.html", {"form": form})


@login_required(login_url='login')
@user_passes_test(check_if_admin)
def pay_grade_update_form(request, pk):
    if request.method == 'POST':
        form = PayGradeForm(request.POST, instance=PayGrade.objects.get(pk=pk))
        if form.is_valid():
            form.save()
            return redirect('pay_grades')
        else:
            return HttpResponse("Error Occurred")
    pay_grade = PayGrade.objects.get(pk=pk)
    form = PayGradeForm(instance=pay_grade)
    return render(request, "admin_view/pay_form.html", {"form": form})


@login_required(login_url='login')
@user_passes_test(check_if_admin)
def delete_department(request, pk):
    department = Department.objects.get(pk=pk)
    department.delete()
    return redirect('departments')


@login_required(login_url='login')
@user_passes_test(check_if_admin)
def delete_pay_grade(request, pk):
    pay_grade = PayGrade.objects.get(pk=pk)
    pay_grade.delete()
    return redirect('pay_grades')
