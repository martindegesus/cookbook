from django.contrib import admin
from .models import *

# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name','picture')
admin.site.register(Recipe,RecipeAdmin)

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name','recipe')
admin.site.register(Ingredients,IngredientAdmin)