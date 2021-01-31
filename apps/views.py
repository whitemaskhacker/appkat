from django.shortcuts import render , redirect
from .forms import SugForm

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = SugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'apps/404.html', {'form' : form})
    else:
        form = SugForm()
    return render(request, 'apps/index.html', {'from' : form})
def car(request):
    if request.method == 'POST':
        form = SugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("error404")
        else:
            return render(request , 'apps/404.html' , {'form' : form})
    else:
        form = SugForm()
    return render(request , 'apps/car.html' , {'form' : form})
def error(request):
    return render(request , 'apps/404.html')