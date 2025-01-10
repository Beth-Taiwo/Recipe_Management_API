from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, Category, Course

# Register your models here.
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
admin.site.register(Ingredient)
admin.site.register(Category)
admin.site.register(Course)
