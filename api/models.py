from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructions = models.TextField()
    preparation_time = models.PositiveIntegerField()
    cooking_time = models.PositiveIntegerField()
    servings = models.IntegerField()
    created_date = models.DateTimeField(auto_now=True)
    ingredients = models.ManyToManyField(Ingredient, through="RecipeIngredient")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    @property
    def total_time(self):
        return self.preparation_time + self.cooking_time
    

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    # quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.ingredient} for {self.recipe.title}"