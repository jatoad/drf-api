from django.db import models
from django.contrib.auth.models import User
from items.models import Item


class Like(models.Model):
    """
    Like model, related to 'owner' and 'item'.
    'owner' is a User instance and 'item' is a Item instance.
    'unique_together' makes sure a user can't like the same item twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(
        Item, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'item']

    def __str__(self):
        return f'{self.owner} {self.item}'
