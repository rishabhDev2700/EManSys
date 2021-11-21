from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('pay-details/', views.pay_details, name="pay_details")
]
