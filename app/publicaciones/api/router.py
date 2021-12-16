from django.urls import path
from publicaciones.api.views import PublicacionApiViewSet

urlpatterns = [
    path('publi/', PublicacionApiViewSet.as_view()),
]