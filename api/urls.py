from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup),
    path('login', views.login),
    path('test_token', views.test_token),
    path('users', views.get_users, name="users"),
    path('users/<int:pk>', views.get_users_by_id),
    path('user/<int:pk>', views.update_user),
    path('user/delete/<int:pk>', views.delete_user),
    path('categories', views.CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='categories'),
    path('ingredients', views.IngredientViewSet.as_view({'get': 'list', 'post': 'create'}), name='ingredients'),
    path('recipes', views.RecipeViewSet.as_view({'get': 'list', 'post': 'create'}), name='recipes'),
    path('recipe/<int:pk>', views.RecipeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='recipe'),
    # path('recipe/<int:pk>/ingredients', views.RecipeIngredientViewSet.as_view({'get': 'list', 'post': 'create'}), name='recipe-ingredients'),
    # path('recipe/ingredient/<int:pk>', views.RecipeIngredientViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='recipe-ingredient'),
]