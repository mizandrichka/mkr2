from django.shortcuts import render, get_object_or_404
from .models import Recipe, Category # Заміни на свої реальні назви моделей, якщо вони інші

# View: main (10 рандомних рецептів)
def main(request):
    random_recipes = Recipe.objects.order_by('?')[:10]
    
    # Передаємо ці рецепти в шаблон під ключем 'recipes'
    return render(request, 'main.html', {'recipes': random_recipes})

# View: category_detail (рецепти певної категорії за id)
def category_detail(request, category_id):
    
    category = get_object_or_404(Category, id=category_id)
    
    recipes = Recipe.objects.filter(category=category)
    
    return render(request, 'category_detail.html', {
        'category': category,
        'recipes': recipes
    })
