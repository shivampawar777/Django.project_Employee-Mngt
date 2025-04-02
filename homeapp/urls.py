from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home),
    path('add-emp/',add_emp),
    path('emp-list/', emp_list),
    path('emp-detail/<int:id>', emp_detail),
    path('emp-update/<int:id>', emp_update),
    path('do-emp-update/<int:id>', do_emp_update)
]

