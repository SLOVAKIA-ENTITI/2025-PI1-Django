from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.zoznam_kruzkov, name='zoznam_kruzkov'),
    path('/form', views.zoznam_kruzkov_form, name='zoznam_kruzkov_form'),
]