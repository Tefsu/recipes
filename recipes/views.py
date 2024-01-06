from django.http import HttpResponse, Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404
from utils.recipes.factory import make_recipe
from recipes.models import Category, Recipe

### FUNCTION BASE TO VIEW
# Create your views here.
def home(request):
    # Return HTTP Response
    # return HttpResponse('Home recipes')

    # categorias = Category.objects.all()
    # print(categorias)

    # categorias.order_by('-id')
    # print(categorias)

    receitas = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    # print(receitas.created_at)
    # print(receitas.updated_at)
    # print(receitas)
    # receitas = get_list_or_404(Recipe, is_published=True)
    # Nao fica bom usar o get list or 404 na home pois se nao houvr resultadso dará o erro 404
    
    return render(request, 'recipes/pages/home.html', status=200, context={
        'recipes': receitas, 
    }) # Recomendado uso de namespace para evitar colisões e confusões no codigo

def recipe(request, id):
    # receita = Recipe.objects.get(id=id)
    receita = get_object_or_404(Recipe, pk=id, is_published=True)
    return render(request, 'recipes/pages/recipe-view.html', status=200, context={
        # 'recipe': make_recipe(),
        'recipe': receita,
        'is_detail_page': True,
    }) # Recomendado uso de namespace para evitar colisões e confusões no codigo

def category(request, category_id):
    receita = get_list_or_404(Recipe.objects.filter(
        is_published=True,
        category__id=category_id
    ).order_by('-id'))

    return render(request, 'recipes/pages/category.html', status=200, context={
        'recipes': receita,
        'title': f'{receita[0].category.name} - Category'
        
    })

# def category(request, category_id):
#     # categoria = Category.objects.all().order_by(id=category_id)
#     # receita = Recipe.objects.filter(
#     #     is_published=True,
#     #     category__id=category_id
#     # ).order_by('-id')

#     # if not receita:
#     #     #metodo 1
#     #     # return HttpResponse(content='Not found', status=404) 
#     #     #metodo 2
#     #     raise Http404('Not found :(')´
#         #metodo 3
    
#     # receita = get_list_or_404(Recipe, category_id=category_id, is_published=True)
#     receita = get_list_or_404(Recipe.objects.filter(
#         is_published=True,
#         category__id=category_id
#     ).order_by('-id'))

#     # category_name = getattr( # Gambiarra
#     #         getattr(receita.first(), 'category', None),
#     #         'name', 
#     #         'Not found'
#     #     )
#     return render(request, 'recipes/pages/category.html', status=200, context={
#         'recipes': receita,
#         'title': f'{receita[0].category.name} - Category'
#         # 'title': f'{category_name} - Category'
        
#     })