from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'detail',
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name="index:user-detail")

    class Meta:
        model = User
        fields = ['username', 'email']