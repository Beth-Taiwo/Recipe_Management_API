from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Recipe, Category, Ingredient, RecipeIngredient

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email','password']
        
    def validate(self, obj):
        if User.objects.filter(username=obj['username']).exists():
            raise serializers.ValidationError("Username already exists.")
        if User.objects.filter(email=obj['email']).exists():
            raise serializers.ValidationError("Email already exists.")
        return obj
    
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
        read_only_fields = ['user']
        
    # def create(self,validated_data):
    #     return Ingredient.objects.create(user=self.context['request'].user, **validated_data)
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
        
    def validate(self, obj):
        if Ingredient.objects.filter(name=obj['name'], user=self.context['request'].user).exists():
            raise serializers.ValidationError("Ingredient already exists for this user.")
        return obj
        
class RecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredient
        fields = ['id', 'recipe', 'ingredient', 'quantity', 'unit']
        

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    course = CategorySerializer(read_only=True)
    
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'instructions', 'preparation_time', 'cooking_time', 'servings', 'created_date', 'ingredients', 'category', 'course']
