from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Item
from .serializers import ItemSerializer, ItemDetailSerializer


class ItemList(generics.ListCreateAPIView):
    """
    List items or create a item if logged in.
    """
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Item.objects.annotate(
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_at')
    
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
    ]

    search_fields = [
        'owner__username',
        'description',
    ]

    ordering_fields = [
        'likes_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an item, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ItemDetailSerializer
    queryset = Item.objects.annotate(
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_at')
