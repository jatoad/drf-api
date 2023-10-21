from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Item
from .serializers import ItemSerializer
from drf_api.permissions import IsOwnerOrReadOnly

class ItemList(APIView):
    serializer_class = ItemSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(
            items, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request):
        serializer = ItemSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
    