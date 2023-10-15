from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    # Return HTTP Response
    # return HttpResponse('Home recipes')
    return render(request, 'recipes/pages/home.html', status=200, context={
        'name': 'Teferson Luan'
    }) # Recomendado uso de namespace para evitar colisões e confusões no codigo

def recipe(request, id):
    # Return HTTP Response
    # return HttpResponse('Home recipes')
    return render(request, 'recipes/pages/recipe-view.html', status=200, context={
        'name': 'Teferson Luan'
    }) # Recomendado uso de namespace para evitar colisões e confusões no codigo
