from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from publicaciones.api.serializers import PublicacionSerializer
from publicaciones.models import Publicacion

class PublicacionApiViewSet(APIView):
    def get(self, request):
        publicaciones = Publicacion.objects.all()
        serializer = PublicacionSerializer(publicaciones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PublicacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        publicacion = Publicacion.objects.get(pk=pk)
        serializer = PublicacionSerializer(publicacion, data=request.data)
        return Response(serializer.data)    