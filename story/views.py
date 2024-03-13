from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Story
from doggo.models import Doggo

class StoryList(ListView):
    """
    Display a list of :model:`story.Story`

    **Context**

    ``story``
        An instance of :model:`story.Story`.

    **Template:**

    :template:`story_list.html`
    """
    queryset = Story.objects.all()
    template_name = "story_list.html"
    context_object_name = "story_list"


class DoggoList(ListView):
   """
   Display a list of :model:`story.Story`

   **Context**

   ``story``
       An instance of :model:`story.Story`.

   **Template:**

   :template:`story_list.html`
   """
   queryset = Doggo.objects.all()
   template_name = "home.html"
   context_object_name = "doggo_list"


def Home(request):
#View based on chatGPT suggestion
    """
    View for the home page, displaying data from both Story and Doggo models.

    **Context**

    ``story_list``
        Queryset containing data from the Story model.

    ``doggo_list``
        Queryset containing data from the Doggo model.

    **Template:**

    :template:`home.html`
    """
    story_list = Story.objects.filter(pinned =1)
    doggo_list = Doggo.objects.exclude(status=0)
    return render(request, 'home.html', {'story_list': story_list, 'doggo_list': doggo_list})

class StoryDetailView(DetailView):
    model = Story
    template_name = 'story_detail.html'

class DoggoDetailView(DetailView):
    model = Doggo
    template_name = 'doggo_detail.html'