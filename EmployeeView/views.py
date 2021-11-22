from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'employee_view/home.html')


def pay_details(request):
    return render(request, 'employee_view/pay_details.html')
