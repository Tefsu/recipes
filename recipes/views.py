from django.http import HttpResponse
from django.shortcuts import render
from utils.recipes.factory import make_recipe

# Create your views here.
def home(request):
    # Return HTTP Response
    # return HttpResponse('Home recipes')
    return render(request, 'recipes/pages/home.html', status=200, context={
        'recipes': [make_recipe() for _ in range(10)]
    }) # Recomendado uso de namespace para evitar colisões e confusões no codigo

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', status=200, context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    }) # Recomendado uso de namespace para evitar colisões e confusões no codigo
