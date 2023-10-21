from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Drawer
from .serializers import DrawerSerializer
from drf_api.permissions import IsOwnerOrReadOnly

class DrawerList(APIView):
    serializer_class = DrawerSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        drawers = Drawer.objects.all()
        serializer = DrawerSerializer(
            drawers, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def Drawer(self, request):
        serializer = DrawerSerializer(
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
    
class DrawerDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = DrawerSerializer

    def get_object(self, pk):
        try:
            drawer = Drawer.objects.get(pk=pk)
            self.check_object_permissions(self.request, drawer)
            return drawer
        except Drawer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        drawer = self.get_object(pk)
        serializer = DrawerSerializer(
            drawer, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        drawer = self.get_object(pk)
        serializer = DrawerSerializer(
            drawer, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        drawer = self.get_object(pk)
        drawer.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
