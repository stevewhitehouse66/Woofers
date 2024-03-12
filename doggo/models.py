from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Registered"), (2, "Assesment"), (3, "Vet-Check")
    , (4, "Ready"), (5, "Fostered"), (6, "Advised"))


SEX = ((0, "Unsexed"), (1, "Female"), (2, "Male"))


NEUTERED = ((0, "No"), (1, "Yes"))
# Create your models here.
# model modified from hackathon project ALLs WELL


class Doggo(models.Model):
    """
    Stores a single dog profile entry related to  :model:`auth.User`
    """
    
    name = models.CharField(max_length=100)
    sex = models.IntegerField(choices=SEX, default=0)
    breed = models.CharField(max_length=100)
    location = models.TextField(max_length=200)
    age = models.IntegerField()
    status = models.IntegerField(choices=STATUS, default=0)
    vet_checked = models.DateTimeField(None)
    vet_note = models.TextField()
    vet_medication = models.TextField()
    vet_vaccinated = models.DateTimeField(None)
    vet_neutered = models.IntegerField(choices=NEUTERED, default=0)
    temperament = models.TextField()
    training = models.TextField()
    behaviour = models.TextField()
    notes = models.TextField()

    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dog_profile")
    profile_image = CloudinaryField('image', default='placeholder')

    
    class Meta:
        ordering = ["added_on"]
    def __str__(self):
        return f"{self.name}.  Breed - {self.breed} added by {self.added_by}"