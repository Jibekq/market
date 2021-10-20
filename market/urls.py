from django.urls import path
from .views import msg, register

urlpatterns = [
    path('', msg,name ='message'),
    path('market/', register, name='register'),        
]