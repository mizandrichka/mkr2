from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    # Головна сторінка
    path('', views.main, name='main'),
    
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
]