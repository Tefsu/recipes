from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views

class RecipeViewsTest(TestCase):
    def test_recipes_home_view_is_correct(self):
        view = resolve(
            reverse('recipes:home')
        )
        self.assertIs(view.func, views.home)

    def test_recipes_home_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipes_home_view_load_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')
        
    def test_recipes_home_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'Não encontramos nenhum resultado por enquanto, tente novamente mais tarde',
            response.content.decode('utf-8')
            ) # decode converte bits em strings
        
    def test_recipes_category_view_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1})
        )
        self.assertIs(view.func, views.category)

    def test_recipes_category_returns_status_code_404_if_no_receipes(self):
        response = self.client.get(
                reverse('recipes:category', kwargs={'category_id': 99999})
            )
        self.assertEqual(response.status_code, 404)

    def test_recipes_recipe_view_is_correct(self):
        view = resolve(
            reverse('recipes:recipe', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.recipe)

    def test_recipes_recipe_view_returns_status_code_404_if_no_receipe(self):
        view = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 99999})
        )
        self.assertEqual(view.status_code, 404)
    