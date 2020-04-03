from rest_framework import viewsets
from . import models
from . import serializers

class Product1Viewset(viewsets.ModelViewSet):
    queryset = models.Product1.objects.all()
    serializer_class = serializers.Product1Serializer

#list(), retrieve(), create(), update(), destroy()    
