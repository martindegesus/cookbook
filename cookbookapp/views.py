from django.shortcuts import render
from .forms import RecipeForm,IngredientsForm
from .models import *
# Create your views here.

def index(request):
    if request.method=='POST':
        if 'submit ingredient' in request.POST:
            form=IngredientsForm(request.POST)
            if form.is_valid():
                if not Ingredients.objects.filter(
                    name=form.cleaned_data['ingredient'],
                    recipe=Recipe.objects.get(name=form.cleaned_data['recipe'])
                    ):
                    ingredient=Ingredients(
                        name=form.cleaned_data['ingredient'],
                        recipe=Recipe.objects.get(name=form.cleaned_data['recipe']),
                        amount=form.cleaned_data['amount'],
                        unit=form.cleaned_data['unit']
                        )
                    ingredient.save()
                else:
                    ing=Ingredients.objects.get(name=form.cleaned_data['ingredient'],recipe=Recipe.objects.get(name=form.cleaned_data['recipe']))
                    ing.amount=form.cleaned_data['amount']
                    ing.unit=form.cleaned_data['unit']
                    ing.save()
        elif 'delete ingredient' in request.POST:
            form=IngredientsForm(request.POST)
            if form.is_valid():
                if not Ingredients.objects.filter(
                    name=form.cleaned_data['ingredient'],
                    recipe=Recipe.objects.get(name=form.cleaned_data['recipe'])
                    ):
                    print('test')
                else:
                    ingredient=Ingredients.objects.get(
                    name=form.cleaned_data['ingredient'],
                    recipe=Recipe.objects.get(name=form.cleaned_data['recipe'])
                    )
                    ingredient.delete()
        elif 'create recipe' in request.POST:
            form=RecipeForm(request.POST, request.FILES)
            if form.is_valid():
                if not Recipe.objects.filter(name=form.cleaned_data['name']):
                    recipe=Recipe(
                        name=form.cleaned_data['name'],
                        description=form.cleaned_data['description'],
                        picture=form.cleaned_data['picture']
                    )
                    recipe.save()
                else:
                    recipe= Recipe.objects.get(name=form.cleaned_data['name'])
                    recipe.picture=form.cleaned_data['picture']
                    recipe.description=form.cleaned_data['description']
                    recipe.save()
        elif 'delete recipe' in request.POST:
            form=RecipeForm(request.POST, request.FILES)
            if form.is_valid():
                if not Recipe.objects.filter(name=form.cleaned_data['name']):
                    print('test')
                else:
                    recipe=Recipe.objects.get(name=form.cleaned_data['name'])
                    recipe.delete()
               
    recipeform=RecipeForm()
    ingredientform=IngredientsForm()
    nonserializedrecipes=Recipe.objects.all()
    recipes=[recipe.serialize() for recipe in nonserializedrecipes]
    print(recipes)
    return render(request, 'cookbookapp/index.html', {'recipes':recipes, 'recipeform':recipeform, 'ingredientform':ingredientform})