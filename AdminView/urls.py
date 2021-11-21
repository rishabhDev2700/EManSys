from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('register/', views.register_user, name="register"),
    path('update/', views.update_user, name="update_user"),
]
