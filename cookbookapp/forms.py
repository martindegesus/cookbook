from cookbookapp.models import Recipe
from django import forms

class RecipeForm(forms.ModelForm):
    class Meta:
        model=Recipe
        fields= '__all__'

class IngredientsForm(forms.Form):
    recipe=forms.CharField(max_length=60)
    ingredient=forms.CharField(max_length=60)
    amount=forms.IntegerField()
    unit=forms.CharField(max_length=60)