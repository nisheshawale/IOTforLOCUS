from .models import TempModel
from rest_framework import viewsets
from .serializers import tempserializer

class TempViewSet(viewsets.ModelViewSet):
    queryset = TempModel.objects.all()
    serializer_class = tempserializer

