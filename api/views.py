from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, CategorySerializer,IngredientSerializer, RecipeSerializer
from rest_framework import viewsets
from .models import Recipe, Category, Ingredient, RecipeIngredient
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import ListAPIView
from django.utils.text import slugify
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'user': serializer.data,'token': token.key})
    return Response(serializer.errors, status=status.HTTP_200_OK)

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'user': serializer.data,'token': token.key })

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed! {}".format(request.user.email))


@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def get_users_by_id(request, pk):
    user = get_object_or_404(User, pk=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['PATCH'])
def update_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
        

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination
    
    def perform_create(self, serializer):
        # Automatically associate the created recipe with the logged-in user
        serializer.save(created_by=self.request.user)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    

class RecipesByCategoryView(ListAPIView):
    """
    API endpoint to filter recipes by category.
    """
    serializer_class = RecipeSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Retrieve the category name from the URL
        category_name = self.kwargs['category']
        # Look up the category object by name
        try:
            category = Category.objects.get(name__iexact=category_name)
        except Category.DoesNotExist:
            # Return an empty queryset if the category doesn't exist
            return Recipe.objects.none()

        # Filter recipes by the category's ID
        return Recipe.objects.filter(category=category)
    

class RecipeByIngredientView(ListAPIView):
    """
    API endpoint to filter recipes by category.
    """
    serializer_class = RecipeSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Retrieve the ingredient name from the URL
        ingredient_name = self.kwargs['ingredient']
        
        # Get all recipes (assuming you have a method to retrieve them as a list of dictionaries)
        all_recipes = self.get_all_recipes()
      
        # Filter recipes by the ingredient name
        filtered_recipes = self.filter_recipes_by_ingredient(all_recipes, ingredient_name)
           
        return filtered_recipes

    def get_all_recipes(self):
        # Fetch all recipes and prefetch related ingredients
        recipes = Recipe.objects.prefetch_related('ingredients')
        return recipes
    

    def filter_recipes_by_ingredient(self, recipes, ingredient_name):
        # Convert ingredient name to lowercase for case-insensitive comparison
        ingredient_name_lower = ingredient_name.lower()
        
        # Filter recipes that contain the ingredient
        filtered_recipes = [
            recipe for recipe in recipes
            if any(slugify(ingredient.name.lower()) == slugify(ingredient_name_lower)
                   for ingredient in recipe.ingredients.all())
        ]
        
        return filtered_recipes

# WIP
class RecipesByMultipleIngredientsView(ListAPIView):
    serializer_class = RecipeSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print(self.request.query_params.get('ingredients', None),'got here')
        # Retrieve the ingredients from the query parameters
        ingredients_param = self.request.query_params.get('ingredients', None)
        if not ingredients_param:
            return Recipe.objects.none()  # Return an empty queryset if no ingredients are provided

        # Split the ingredients into a list
        ingredient_names = [ingredient.strip() for ingredient in ingredients_param.split(',')]

        # Filter recipes that contain all the specified ingredients
        return (
            Recipe.objects.annotate(ingredient_count=Count('ingredients'))
            .filter(ingredients__name__in=ingredient_names)
            .distinct()
            .filter(ingredient_count=len(ingredient_names))  # Ensure all specified ingredients are present
        )
        

class RecipeSearchView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    
    # Allow ordering by fields like cooking_time, servings, etc.
    ordering_fields = ['cooking_time', 'preparation_time', 'servings']
    search_fields = ['title','category__name','ingredients__name','preparation_time']
    filterset_fields= ['cooking_time', 'preparation_time', 'servings']