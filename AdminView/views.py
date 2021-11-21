from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return render(request, 'admin/dashboard.html')


def register_user(request):
    return render(request, 'admin/user_form.html', {})


def update_user(request):
    return render(request, 'admin/user_form.html', {})
