from django.urls import path
# from recipes.views import home
from . import views # metodo para não ter que ir importando view por view na mão

urlpatterns = [
    path('', views.home), # Home
    path('recipes/<int:id>/', views.recipe), 
]