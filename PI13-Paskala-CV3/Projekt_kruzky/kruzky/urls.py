from django.urls import path
from . import views

urlpatterns = [
    path('', views.zoznam_kruzkov, name='zoznam_kruzkov'),

    path('prihlaska/', views.prihlaska_view, name='prihlaska'),
    path('success/', views.success_view, name='success'),
    path('pridat-kruzok/', views.pridat_kruzok_view, name='pridat_kruzok'),
    path('kruzok/zmazat/<int:id>/', views.zmazat_kruzok, name='zmazat_kruzok'),
]