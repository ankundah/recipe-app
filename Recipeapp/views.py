from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
import requests
from django.core.paginator import Paginator
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from .serializers import recipeserializer 
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Recipe

# API_KEY = "95ab8203422b4c88b570767bd22eb460"
# BASE_URL = "https://api.spoonacular.com/recipes/"

API_KEY = "1"
BASE_URL = "http://www.themealdb.com/api/json/v1/1/search.php?s=" 


def search_recipes(request):
    query = request.GET.get('query')
    if query:
        response = requests.get(f'{BASE_URL} {query}')
        data = response.json()
    
    paginator = Paginator(data['meals'], 2)  # Show 2 recipes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'search.html', {'page_obj': page_obj, 'recipes': data['meals'],'query': query})
    

def search(request):
    return render(request, "search.html")

@method_decorator(csrf_exempt, name='dispatch')
class recipeCreateView(CreateAPIView):
    serializer_class = recipeserializer

class recipeListView(ListAPIView):
    serializer_class = recipeserializer
    queryset = Recipe.objects.all()

def create_recipe(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        ingredients = request.POST.get('ingredients')
        image = request.FILES.get('image')  
        description = request.POST.get('description')
        Recipe.objects.create(name=name, description=description, ingredients=ingredients, image=image)
        return redirect('recipe_list')
    return render(request, 'home.html')

def recipe_list(request):
    recipes = Recipe.objects.all()
    tab_name = request.GET.get('recipeList', 'default_tab')
    return render(request, 'home.html', {'recipes': recipes,'tab_name': tab_name})

class recipeUpdateView(UpdateAPIView):
    serializer_class = recipeserializer
    queryset = Recipe.objects.all()
    lookup_field = 'name'

class recipeDeleteView(DestroyAPIView):
    serializer_class = recipeserializer
    queryset = Recipe.objects.all()
    lookup_field = 'name'

class recipeRetrieveView(RetrieveAPIView):
    serializer_class = recipeserializer
    queryset = Recipe.objects.all()
    lookup_field = 'name'

def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        ingredients = request.POST.get('ingredients')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        
        recipe.name = name
        recipe.ingredients = ingredients
        recipe.description = description
        
        if image:
            recipe.image = image
        
        recipe.save()
        return redirect('recipe_list')
    
    context = {
        'recipe': recipe
    }
    return render(request, 'edit_recipe.html', context)