from django import views
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('api/recipes/search/', views.search_recipes, name='search-recipe'),
path('api/create-recipe/', views.recipeCreateView.as_view(), name='create-recipe'),
path('api/list-recipes/', views.recipeListView.as_view(), name='list-view'),
path('api/<str:name>/', views.recipeRetrieveView.as_view(), name='recipe'),
path('api/<str:name>/update', views.recipeUpdateView.as_view(), name='update-recipe'),
path('api/<str:name>/delete', views.recipeDeleteView.as_view(), name='delete-recipe'),
path('recipes/search/', views.search, name='search'),
path('recipes/home/', views.create_recipe, name='create-ui'),
path('recipes/home/list', views.recipe_list, name='recipe_list'),
path('recipes/home/?tab=<str:tab_name>/', views.recipe_list, name='list_tab'),
path('edit-recipe/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
]

if settings.DEBUG:
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)