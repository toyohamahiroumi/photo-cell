from django.db import models
from users.models import User
from taggit.managers import TaggableManager


class Photo(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image')
    comment = models.TextField(blank='True')
    created_at = models.DateTimeField(auto_now=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title
