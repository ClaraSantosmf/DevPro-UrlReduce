
from django.contrib import admin
from django.urls import path
from devpro.encurtador import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('<slug:slug>', views.redirecionador),
    path('relatorio/<slug:slug>', views.relatorio, name='relatorio'),
    path('registrado/', views.registrado, name='registrado'),
]
