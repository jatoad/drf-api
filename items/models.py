from django.db import models
from django.contrib.auth.models import User
from drawers.models import Drawer


class Item(models.Model):
    """
    Item model, related to User and Drawer
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    drawer = models.ForeignKey(Drawer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField()
    image = models.ImageField(
        upload_to='images/', default='../default_profile_mx0cj', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.description