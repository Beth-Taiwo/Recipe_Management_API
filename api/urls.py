from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='categories')
router.register('ingredients', views.IngredientViewSet, basename='ingredients')
router.register('recipes', views.RecipeViewSet, basename='recipes')

# router.register('recipe-ingredients', views.RecipeIngredientViewSet)  # TODO

urlpatterns = [
    path('signup', views.signup),
    path('login', views.login),
    path('test_token', views.test_token),
    path('users', views.get_users, name="users"),
    path('users/<int:pk>', views.get_users_by_id),
    path('user/<int:pk>', views.update_user),
    path('user/delete/<int:pk>', views.delete_user),
    path('', include(router.urls)),
    path('recipes/category/<str:category>/', views.RecipesByCategoryView.as_view(), name='recipes-by-category'),
     # path('recipe/<int:pk>/ingredients', views.RecipeIngredientViewSet.as_view({'get': 'list', 'post': 'create'}), name='recipe-ingredients'),
    # path('recipe/ingredient/<int:pk>', views.RecipeIngredientViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='recipe-ingredient'),
]