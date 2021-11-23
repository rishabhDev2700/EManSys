from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

from Authentication.models import PayGrade
from .decorators import check_if_not_admin


# Create your views here.
@login_required(login_url='login')
@user_passes_test(check_if_not_admin)
def home(request):
    return render(request, 'employee_view/home.html')


@login_required(login_url='login')
@user_passes_test(check_if_not_admin)
def pay_details(request):
    pay = request.user.pay_grade
    return render(request, 'employee_view/pay_details.html', {'pay': pay})
