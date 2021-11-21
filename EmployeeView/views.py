from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'templates/employee/home.html')


def pay_details(request):
    return render(request, 'templates/employee/pay_details.html')
