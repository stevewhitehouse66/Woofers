from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Story
from doggo.models import Doggo
from .forms import StoryForm
from doggo.forms import DoggoForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Contact View


def ContactView(request):
    return render(request, 'contact.html')


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
    story_list_pinned = Story.objects.filter(pinned=1)
    story_list_published = Story.objects.filter(status=1, pinned=0)
    doggo_list = Doggo.objects.exclude(status=0)
    return render(request, 'home.html', {'story_list_pinned': story_list_pinned,
                                         'story_list_published': story_list_published,
                                         'doggo_list': doggo_list})


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


@login_required
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
            messages.add_message(
                request, messages.SUCCESS,
                'New Story Saved'
                )
            return redirect('/story')
    else:
        form = StoryForm()

    return render(request, 'story_form.html', {'form': form})


@login_required
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
            messages.add_message(
                request, messages.SUCCESS,
                'New Dog Profile Submitted'
                )
            return redirect('/doggo')
    else:
        form = DoggoForm()

    return render(request, 'doggo_form.html', {'form': form})


# Update Views (Based on ChatGPT suggestion to stop message double firing)


class StoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Edit an instance of :model:`story.Story`.

    **Template:**
    :form:'/story/forms.py
    :template:`story_edit_form.html`
    """
    model = Story
    fields = ['title',  'content', 'excerpt', 'status', 'pinned']
    template_name = 'story_edit_form.html'
    success_url = reverse_lazy('story')

    def get_success_message(self, cleaned_data):
        return "Dog Profile updated successfully."

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class DoggoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
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

    def get_success_message(self, cleaned_data):
        return "Doggo details updated successfully."

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class StoryDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """
    Delete an individual story.

    **Context**

    ``post``
        An instance of :model:`story.Story`.
    """
    model = Story
    template_name = 'confirm_delete_form.html'
    success_url = reverse_lazy('story')

    def get_success_message(self, cleaned_data):
        return "Story Deleted successfully."


class DoggoDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """
    Delete an individual dog profile.

    **Context**

    ``post``
        An instance of :model:`doggo.Doggo`.
    """
    model = Doggo
    template_name = 'confirm_delete_form.html'
    success_url = reverse_lazy('doggos')

    def get_success_message(self, cleaned_data):
        return "Dog Profile Deleted successfully."
