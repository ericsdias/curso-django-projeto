from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
<<<<<<< HEAD
    return render(request, 'recipes/pages/home.html')

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html')
=======
    return render(request, 'recipes/pages/home.html')
>>>>>>> 38d6e5a86f3185056e66767df0eaa44322017b6a
