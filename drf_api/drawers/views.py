from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Drawer
from .serializers import DrawerSerializer


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

    def post(self, request):
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