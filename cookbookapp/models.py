from django.db import models

# Create your models here.

class Recipe(models.Model):
    name=models.CharField(max_length=60)
    description=models.CharField(max_length=400)
    picture=models.ImageField(null=True,blank=True)

    def serialize(self):
        ingredients=[]
        for ingredient in Ingredients.objects.filter(recipe=self):
            ingredients.append(ingredient)
        return{
            'name': self.name,
            'description':self.description,
            'picture':self.picture,
            'ingredients': ingredients
        }

class Ingredients(models.Model):
    name=models.CharField(max_length=60)
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE)
    amount=models.IntegerField(default=0)
    unit=models.CharField(max_length=60, null=True)