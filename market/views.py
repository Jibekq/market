from django.shortcuts import render

from .forms import  RegistrationForm

def helloworld(request):
    return render(request, 'registration.html')

def register(request):
    form = RegistrationForm(request.POST or None)
    message = 'Fill the blank'
    if request.method =='POST' and form.is_valid():
        message = 'Your name and surname was successfully uploaded'
        form.save()
        return render(request, 'registration.html', {'form': form, 'message':message})
    return render(request, 'registration.html', {'form': form, 'message':message})
    

