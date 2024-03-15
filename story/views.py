from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView , DetailView, CreateView
from .models import Story
from doggo.models import Doggo
from .forms import StoryForm
from doggo.forms import DoggoForm

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
   template_name = "doggo_list.html"
   context_object_name = "doggo_list"


def Home(request):
#View based on chatGPT suggestion for using data from 2 models in a single view
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



def StoryCreate(request):
    
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success-url')
    else:
        form = StoryForm()
    
    return render(request, 'story_form.html', {'form': form})

def DoggoCreate(request):
    
    if request.method == 'POST':
        form = DoggoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success-url')
    else:
        form = DoggoForm()
    
    return render(request, 'doggo_form.html', {'form': form})