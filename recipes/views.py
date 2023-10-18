from django.http import HttpResponse
from django.shortcuts import render
from utils.recipes.factory import make_recipe
from recipes.models import Category, Recipe

# Create your views here.
def home(request):
    # Return HTTP Response
    # return HttpResponse('Home recipes')

    # categorias = Category.objects.all()
    # print(categorias)

    # categorias.order_by('-id')
    # print(categorias)

    receitas = Recipe.objects.all().order_by('-id')
    # print(receitas.created_at)
    # print(receitas.updated_at)
    # print(receitas)
    
    return render(request, 'recipes/pages/home.html', status=200, context={
        'recipes': receitas, 
    }) # Recomendado uso de namespace para evitar colisões e confusões no codigo

def recipe(request, id):
    receita = Recipe.objects.get(id=id)
    return render(request, 'recipes/pages/recipe-view.html', status=200, context={
        'recipe': receita,
        'is_detail_page': True,
    }) # Recomendado uso de namespace para evitar colisões e confusões no codigo

def category(request, category_id):
    # categoria = Category.objects.all().order_by(id=category_id)
    receita = Recipe.objects.filter(
        category__id=category_id
    ).order_by('-id')
    
    return render(request, 'recipes/pages/home.html', status=200, context={
        'recipes': receita,
    }) #