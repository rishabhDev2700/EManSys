from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_dashboard, name="dashboard"),
    path('register/', views.register_user, name="register"),
    path('update/', views.update_user, name="update_user"),
    path('delete/', views.delete_user, name="delete_user"),
    path('departments/', views.get_departments, name="departments"),
    path('paygrades/', views.get_pay_grades, name="pay_grades"),
]
