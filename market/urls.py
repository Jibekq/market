from django.urls import path
from .views import helloworld, register

urlpatterns = [
    path('', helloworld,name ='message'),
    path('registrationform/', register, name='register'),        
]