from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home, name='home'),
    path('story_detail/<int:pk>/', views.StoryDetailView.as_view(), name='story_detail'),
    path('doggo_detail/<int:pk>/', views.DoggoDetailView.as_view(), name='doggo_detail'),
    path('story/', views.StoryList.as_view(), name='story'),
    path('doggo/', views.DoggoList.as_view(), name='doggos'),
    
#CRUD for Stories
    path('story/add/', views.StoryCreate, name='story_add'),
    path('edit/', views.DoggoList.as_view(), name='edit'),
    path('delete/', views.DoggoList.as_view(), name='delete'),

#CRUD for Doggos
    path('add/', views.DoggoCreate, name='doggo_add'),
    path('edit/', views.DoggoList.as_view(), name='edit'),
    path('delete/', views.DoggoList.as_view(), name='delete'),

    ]