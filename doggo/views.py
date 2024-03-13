from django.shortcuts import render
from django.views.generic import ListView
from .models import Doggo
# Create your views here.


class DoggoList(ListView):
   """
   Display a list of :model:`story.Story`

   **Context**

   ``story``
       An instance of :model:`story.Story`.

   **Template:**

   :template:`story_list.html`
   """
   queryset = Doggo.objects.filter()
   template_name = "doggo_list.html"