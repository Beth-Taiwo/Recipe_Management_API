from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup),
    path('login', views.login),
    path('test_token', views.test_token),
    path('users', views.get_users, name="users"),
    path('users/<int:pk>', views.get_users_by_id),
]