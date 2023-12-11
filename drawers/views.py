from django.db.models import Count
from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Drawer
from .serializers import DrawerSerializer

class DrawerList(generics.ListCreateAPIView):
    """
    List drawers or create a drawer if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = DrawerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Drawer.objects.annotate(
        items_count=Count('item', distinct=True)
    ).order_by('-created_at')

    ordering_fields = [
        'items_count',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DrawerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = DrawerSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Drawer.objects.all()