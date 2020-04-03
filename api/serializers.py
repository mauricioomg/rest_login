from rest_framework import serializers
from .models import Product1


class Product1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product1
        fields = '__all__'