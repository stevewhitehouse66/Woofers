from django import forms
from .models import Doggo


class DoggoForm(forms.ModelForm):

    class Meta:
        model = Doggo
        fields = ['profile_image', 'name', 'sex', 'breed', 'age', 'location',
                  'status', 'vet_checked', 'vet_note', 'vet_vaccinated',
                  'vet_neutered', 'vet_weight', 'temperament', 'training',
                  'behaviour', 'notes']

        widgets = {
            'vet_checked': forms.DateInput(attrs={'format': 'yyyy-mm-dd',
                                                  'type': 'date'}),
            'vet_vaccinated': forms.DateInput(attrs={'format': 'yyyy-mm-dd',
                                                     'type': 'date'}),
        }
        vet_vaccinated = forms.DateField(required=False)
        vet_checked = forms.DateField(required=False)

