from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # main form page
    path('result/', views.result, name='result'),  # show score result
]
