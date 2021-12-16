from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from myapp.serializers import UserSerializer, PasswordSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['post'])
    def set_password(self, request, pk = None):
        user = self.get_object()
        serializer = PasswordSerializer(data = request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    @action(detail = False)
    def recent_users(self, request):
        recent_users = User.objects.all().order_by('-last_login')

        page = self.paginate_queryset(recent_users)
        if page is not None:
            serializer = self.get_serializer(page, many = True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_users, many = True)
        return Response(serializer.data) @action(detail = True, methods = ['put'], name = 'Change Password')
    
    def password(self, request, pk = None):
        """Update the user's password."""

    @password.mapping.delete
    def delete_password(self, request, pk = None):
        """Delete the user's password."""
        
"""
Actions
The following actions are handled by the router class by default:

1. list
2. create
3. retrieve (pk needed)
4. update (pk needed)
5. partial_update (pk needed)
6. destroy (pk needed)

You can also create custom actions with the @action decorator.
Example
"""    
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

#ViewSet

"""
The ViewSet class takes advantage of the APIView class.
It doesn't provide any actions by default, but you can use it to create your own set of views:
"""

class ItemsViewSet(ViewSet):
    queryset = Item.objects.all()

    def list(self, request):
        serializer = ItemSerializer(self.queryset, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        item = get_object_or_404(self.queryset, pk = pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    @action(detail = False, methods = ['get'])
    def items_not_done(self, request):
        user_count = Item.objects.filter(done = False).count()
        return Response(user_count)    
    
    
#ModelViewSet

"""
ModelViewSet provides default create, retrieve, update, partial_update, destroy and list actions since it uses GenericViewSet and all of the available mixins.
ModelViewSet is the easiest of all the views to use. You only need three lines:
"""    
class ItemModelViewSet(ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()