from . import views
from django.urls import path


urlpatterns = [
    path(
        'doggo_detail/<int:pk>/',
        views.DoggoDetailView.as_view(),
        name='doggo_detail'),
    path('', views.DoggoList.as_view(), name='doggos'),
    path('doggo/add/', views.DoggoCreate, name='doggo_add'),
    path('doggo/<int:pk>/update/', views.DoggoUpdateView.as_view(),
         name='doggo_edit'),
    path('doggo/<int:pk>/delete/', views.DoggoDeleteView.as_view(),
         name='doggo_delete'),
]
