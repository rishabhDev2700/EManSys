from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_dashboard, name="dashboard"),
    path('register/', views.register_user, name="register"),
    path('update/', views.update_user, name="update_user"),
    path('delete/', views.delete_user, name="delete_user"),
    path('departments/', views.get_departments, name="departments"),
    path('departments/delete/<int:id>', views.delete_department, name="department_delete"),
    path('departments/form', views.department_form, name='department_form'),
    path('paygrades/', views.get_pay_grades, name="pay_grades"),
    path('paygrades/delete/<int:id>', views.delete_pay_grade, name="pay_grade_delete"),
    path('paygrades/form', views.pay_grade_form, name='pay_grade_form')
]
