from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse


# Create your models here.
# model reused from hackathon project ALLs WELL
STATUS = ((0, "Draft"), (1, "Published"))
PINNED = ((0, "No"), (1, "Yes"))


class Story(models.Model):
    """
    Stores a single story entry related to  :model:`auth.User`
    """
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="stories")
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    pinned = models.IntegerField(choices=PINNED, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Story {self.title} written by {self.author}"

    def get_absolute_url(self):
        return reverse('story:story_list', kwargs={'pk': self.pk})
