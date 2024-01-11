from django.test import TestCase
from django.urls import reverse, resolve
from . import views

# Create your tests here.
class RecipeURLsTest(TestCase):

    def test_recipes_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_recipes_category_url_is_correct(self):
        # args = argumentos em ordem, kwargs, manda dicionario e passa o id
        url = reverse('recipes:category', kwargs={'category_id': 1}) 
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipes_recipe_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1/')

    # def test_pytest_is_ok(self):
    #     assert 1 == 1, 'um nao é igual a dois'
    #     nome = 'tefsu'
    #     if nome:
    #         print(nome)

class RecipeViewsTest(TestCase):
    def test_recipes_home_view_is_correct(self):
        view = resolve(
            reverse('recipes:home')
        )
        self.assertIs(view.func, views.home)

    def test_recipes_category_view_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1})
        )
        self.assertIs(view.func, views.category)

    def test_recipes_recipe_view_is_correct(self):
        view = resolve(
            reverse('recipes:recipe', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.recipe)