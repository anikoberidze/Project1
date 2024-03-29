from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('food/', views.food, name='food'),
    path('edit_food/<int:food_id>/', views.edit_food, name='edit_food'),
    path('add_food/', views.add_food, name='add_food'),
]
