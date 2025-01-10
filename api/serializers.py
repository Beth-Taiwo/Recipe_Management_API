from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Recipe, Category, Ingredient, RecipeIngredient,Course

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
       
        
class RecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredient
        fields = '__all__'
        

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = serializers.PrimaryKeyRelatedField(queryset=Ingredient.objects.all(), many=True)
    category = serializers.StringRelatedField()
    course = serializers.StringRelatedField()
    
    class Meta:
        model = Recipe
        fields = '__all__'
        read_only_fields = ['created_date', 'created_by']
    
    def to_representation(self, instance):
        """
        Customize the representation to include full ingredient details in the response.
        """
        representation = super().to_representation(instance)
        representation['ingredients'] = IngredientSerializer(
            instance.ingredients.all(), many=True
        ).data
        return representation