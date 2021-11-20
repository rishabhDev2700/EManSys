from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, "login.html", {})


def logout_user(request):
    logout(request)
    return redirect('login')


def register_user(request):
    return render(request, 'user_form.html', {})


def update_user(request):
    return render(request, 'user_form.html', {})
