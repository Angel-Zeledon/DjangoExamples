from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from login.api.serializers import UsuarioSerializer, RegisterSerializer
from login.models import Usuario

class UsuarioApiViewSet(APIView):

    def get(self,request,pk):
        user = Usuario.objects.get(id = pk)
        print(user)
        serializer = UsuarioSerializer(user)
        return Response(serializer.data, status = status.HTTP_200_OK)

        
    def post(self, request):
        serializer = UsuarioSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)    

class RegisterApiViewSet(APIView):

    def get(self, request, formate = None):
        users = Usuario.objects.all()
        serializer = RegisterSerializer(users, many = True)
        print(serializer.data)
        return Response(serializer.data, status = status.HTTP_200_OK)
        
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            print("Se guardó correctamente", serializer.data)
            return Response(serializer.data)
        return Response(serializer.erros, status = status.HTTP_400_BAD_REQUEST)            





