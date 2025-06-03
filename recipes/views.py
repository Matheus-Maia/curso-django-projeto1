from django.shortcuts import render
from utils.recipes.factory import make_recipes

# Create your views here.
def home(request):
    return render(request, 'recipes/pages/home.html', context={'recipes': [make_recipes() for _ in range(10)]}) # < gera 10 receitas com a fabrica

def recipes(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={'recipe': make_recipes()})