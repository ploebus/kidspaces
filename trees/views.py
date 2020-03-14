from django.shortcuts import render
# from django.views.generic import TemplateView
from .models import Trees
from .forms import TreeForm
# Create your views here.

def HomePageView(request):
    trees = Trees.objects.all()
    if request.method == "POST":
        form = TreeForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    

        
        
    else:
        
        form = TreeForm()
    return render(request, 'home.html', {'trees':trees, 'form':form})
	  