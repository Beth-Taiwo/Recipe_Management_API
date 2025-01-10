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
    # unit = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)
    instructions = models.TextField()
    preparation_time = models.PositiveIntegerField(blank=True,default=0)
    cooking_time = models.PositiveIntegerField(blank=True, default=0)
    servings = models.IntegerField(blank=True, default=0)
    created_date = models.DateTimeField(auto_now=True)
    ingredients = models.ManyToManyField(Ingredient, through="RecipeIngredient", blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    
    def __str__(self):
        return f"{self.created_by} created the {self.title} recipe"
    
    @property
    def total_time(self):
        return self.preparation_time + self.cooking_time
    

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    # quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return f"{self.recipe.title} with {self.ingredient} of {self.unit} quantity"