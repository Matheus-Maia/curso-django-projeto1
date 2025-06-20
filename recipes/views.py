from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe


# Create your views here.
def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id') # < pega a receita mais recente
    return render(request, 'recipes/pages/home.html', context={'recipes': recipes})

def category(request, category_id):
    recipes = Recipe.objects.filter(
        category_id=category_id, is_published=True
        ).order_by('-id') 
    return render(request, 'recipes/pages/category.html', context={'recipes': recipes,
                                                               })


def recipes(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={'recipe': make_recipe(),
    'is_detail_page': True,                                                                      
    })