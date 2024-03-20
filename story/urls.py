from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home, name='home'),
    path('contact/', views.ContactView, name='contact'),
    path(
        'story_detail/<int:pk>/',
        views.StoryDetailView.as_view(),
        name='story_detail'),
    path(
        'doggo_detail/<int:pk>/',
        views.DoggoDetailView.as_view(),
        name='doggo_detail'),
    path('story/', views.StoryList.as_view(), name='story'),
    path('doggo/', views.DoggoList.as_view(), name='doggos'),

    # CRUD for Stories
    path('story/add/', views.StoryCreate, name='story_add'),
    path('story/<int:pk>/update/', views.StoryUpdateView.as_view(), name='story_edit'),
    path('story/<int:pk>delete/', views.StoryDeleteView.as_view(), name='story_delete'),

    # CRUD for Doggos
    path('add/', views.DoggoCreate, name='doggo_add'),
    path('doggo/<int:pk>/update/', views.DoggoUpdateView.as_view(), name='doggo_edit'),
    path('doggo/<int:pk>/delete/', views.DoggoDeleteView.as_view(), name='doggo_delete'),

]
