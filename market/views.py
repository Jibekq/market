from django.shortcuts import render

from .forms import Regform

def msg(request):
    return render(request, 'start.html')

def register(request):
    form = Regform(request.POST or None)
    message = 'fill the blank'
    if request.method =='POST' and form.is_valid():
        message = 'Good'
        form.save()
        return render(request, 'start.html', {'form': form, 'message':message})
    return render(request, 'start.html', {'form': form, 'message':message})
    

