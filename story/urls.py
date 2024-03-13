from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home, name='home'),
    path('story/', views.StoryList.as_view(), name='story'),
    path('doggo/', views.StoryList.as_view(), name='doggo'),
    ]