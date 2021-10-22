from django.shortcuts import render

from .forms import  RegistrationForm

def helloworld(request):
    return render(request, 'start.html')

def register(request):
    form = RegistrationForm(request.POST or None)
    message = 'Fill the blank'
    if request.method =='POST' and form.is_valid():
        message = 'Good'
        form.save()
        return render(request, 'start.html', {'form': form, 'message':message})
    return render(request, 'start.html', {'form': form, 'message':message})
    

