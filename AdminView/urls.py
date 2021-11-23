from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_dashboard, name="dashboard"),
    path('register/', views.register_user, name="register"),
    path('update/<int:pk>/', views.update_user, name="update_user"),
    path('delete/<int:pk>/', views.delete_user, name="delete_user"),
    path('departments/', views.get_departments, name="departments"),
    path('departments/delete/<int:pk>/', views.delete_department, name="department_delete"),
    path('departments/form/', views.department_form, name='department_form'),
    path('departments/update/<int:pk>/', views.department_update_form, name='department_update'),
    path('paygrades/', views.get_pay_grades, name="pay_grades"),
    path('paygrades/delete/<int:pk>/', views.delete_pay_grade, name="pay_grade_delete"),
    path('paygrades/form', views.pay_grade_form, name='pay_grade_form'),
    path('paygrades/update/<int:pk>/', views.pay_grade_update_form, name='pay_grade_update'),
]
