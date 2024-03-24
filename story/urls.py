from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home, name='home'),
    path('contact/', views.ContactView, name='contact'),
    path(
        'story_detail/<int:pk>/',
        views.StoryDetailView.as_view(),
        name='story_detail'),
    path('story/', views.StoryList.as_view(), name='story'),
    path('story/add/', views.StoryCreate, name='story_add'),
    path('story/<int:pk>/update/', views.StoryUpdateView.as_view(),
         name='story_edit'),
    path('story/<int:pk>delete/', views.StoryDeleteView.as_view(),
         name='story_delete'),
]
