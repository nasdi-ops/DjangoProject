from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('',  views.home, name='home'),
    path('success',  views.success, name='success'),
    path('taken',  views.taken, name='taken')
    
]