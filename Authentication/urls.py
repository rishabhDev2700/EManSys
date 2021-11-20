from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('update/', views.update_user, name="update_user"),
]
