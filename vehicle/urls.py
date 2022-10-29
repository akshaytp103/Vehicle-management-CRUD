import django
from django import views

from django.urls import path
from . import views

urlpatterns=[
    
    path('list',views.Vehicle_list,name='list'),
    path('', views.Vehicle_form,name='vehicle_add'),
    path('<int:id>/', views.Vehicle_form,name='vehicle_update'),
    path('delete/<int:id>/',views.vehicle_delete,name='vehicle_delete'),
]