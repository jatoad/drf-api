from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Item
from .serializers import ItemSerializer, ItemDetailSerializer


class ItemList(generics.ListCreateAPIView):
    """
    List items or create a item if logged in.
    """
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Item.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an item, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ItemDetailSerializer
    queryset = Item.objects.all()
