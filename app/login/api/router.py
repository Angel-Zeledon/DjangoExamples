from django.urls import path
from login.api.views import UsuarioApiViewSet, RegisterApiViewSet

urlpatterns = [
    path('login/<int:pk>', UsuarioApiViewSet.as_view()),
    path('register/', RegisterApiViewSet.as_view())
]