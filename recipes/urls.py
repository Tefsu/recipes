from django.urls import path
# from recipes.views import home
from . import views # metodo para não ter que ir importando view por view na mão

# name space para urls 
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'), # Home
    path('recipes/<int:id>/', views.recipe, name='recipe'), 
]