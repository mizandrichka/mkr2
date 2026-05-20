from django.test import TestCase
from django.urls import reverse
from .models import Category, Recipe

class RecipeViewsTest(TestCase):
    def setUp(self):

        self.category = Category.objects.create(name="Тестова категорія")
        
        # 11 рецептів, щоб перевірити, чи головна сторінка показує рівно 10
        for i in range(11):
            Recipe.objects.create(
                title=f"Рецепт {i}",
                description="Опис",
                instructions="Інструкція",
                ingredients="Інгредієнти",
                category=self.category
            )

    def test_main_view(self):

        response = self.client.get(reverse('recipe:main'))
        
        self.assertEqual(response.status_code, 200)
        
        self.assertTemplateUsed(response, 'main.html')
        
        self.assertTrue('recipes' in response.context)
        self.assertEqual(len(response.context['recipes']), 10)

    def test_category_detail_view(self):

        url = reverse('recipe:category_detail', args=[self.category.id])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        
        self.assertTemplateUsed(response, 'category_detail.html')
        
        self.assertEqual(response.context['category'].name, "Тестова категорія")
        
        self.assertEqual(len(response.context['recipes']), 11)