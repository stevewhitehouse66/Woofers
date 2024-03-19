from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView

from .models import Story
from doggo.models import Doggo
from .forms import StoryForm
from doggo.forms import DoggoForm
from django.urls import reverse_lazy
from django import forms
# List Views


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

# Home view, mix of both models


def Home(request):
    # View based on chatGPT suggestion for using data from 2 models in a
    # single view
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
    story_list = Story.objects.filter(pinned=1)
    doggo_list = Doggo.objects.exclude(status=0)
    return render(request, 'home.html', {'story_list': story_list,
                                         'doggo_list': doggo_list})

# Detail Views


class StoryDetailView(DetailView):
    """
    Display an instance of :model:`story.Story`.

    **Context**

    **Template:**

    :template:`story_detail.html`
    """
    model = Story
    template_name = 'story_detail.html'


class DoggoDetailView(DetailView):
    """
    Display an instance of :model:`doggo.Doggo`.

    **Context**

    **Template:**

    :template:`doggo_detail.html`
    """
    model = Doggo
    template_name = 'doggo_detail.html'

# Create Views


def StoryCreate(request):
    """
    Create an instance of :model:`doggo.Doggo`.

    **Template:**
    :form:'/story/forms.py
    :template:`story_form.html`
    """
    if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            logged_in_user = request.user
            story_instance = form.save(commit=False)
            story_instance.author = logged_in_user
            story_instance.save()
            return redirect('/story')
    else:
        form = StoryForm()

    return render(request, 'story_form.html', {'form': form})



def DoggoCreate(request):
    """
    Create an instance of :model:`doggo.Doggo`.

    **Template:**
    :form:'/doggo/forms.py
    :template:`doggo_form.html`
    """
    if request.method == 'POST':
        form = DoggoForm(request.POST, request.FILES)
        if form.is_valid():
            logged_in_user = request.user
            doggo_instance = form.save(commit=False)
            doggo_instance.added_by = logged_in_user
            doggo_instance.save()
            return redirect('/doggo')
    else:
        form = DoggoForm()

    return render(request, 'doggo_form.html', {'form': form})


# Update Views (Based on ChatGPT suggestion)


class StoryUpdateView(UpdateView):
    """
    Edit an instance of :model:`story.Story`.

    **Template:**
    :form:'/story/forms.py
    :template:`story_edit_form.html`
    """
    model = Story
    fields = ['title',  'content', 'excerpt']
    template_name = 'story_edit_form.html'
    success_url = reverse_lazy('story')


class DoggoUpdateView(UpdateView):
    """
    Edit an instance of :model:`doggo.Doggo`.

    **Template:**
    :form:'/doggo/forms.py
    :template:`doggo_edit_form.html`
    """
    model = Doggo
    fields = ['name', 'sex', 'breed', 'age', 'location',
                  'status', 'vet_checked', 'vet_note', 'vet_vaccinated',
                  'vet_neutered', 'vet_weight', 'temperament', 'training',
                  'behaviour', 'notes']
    template_name = 'doggo_edit_form.html'
    success_url = reverse_lazy('doggos')
