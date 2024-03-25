from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Doggo
from .forms import DoggoForm
from django.urls import reverse_lazy
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
    queryset = Doggo.objects.all()
    template_name = "doggo_list.html"
    context_object_name = "doggo_list"


class DoggoDetailView(DetailView):
    """
    Display an instance of :model:`doggo.Doggo`.

    **Context**

    **Template:**

    :template:`doggo_detail.html`
    """
    model = Doggo
    template_name = 'doggo_detail.html'


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
            return redirect('doggos')
    else:
        form = DoggoForm()

    return render(request, 'doggo_form.html', {'form': form})

# Update Views (Based on ChatGPT suggestion to stop message double firing)


class DoggoUpdateView(SuccessMessageMixin, UpdateView):
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


class DoggoDeleteView(SuccessMessageMixin, DeleteView):
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