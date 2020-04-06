from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, viewsets, permissions
from django.views.generic import TemplateView, ListView
from rest_framework.permissions import IsAuthenticated
from apps.index.serializers import UserSerializer
from .serializers import ProductSerializer
from django.contrib.auth.models import User
from .models import Product
import requests



class IndexView(TemplateView):
    template_name = "index.html"

class RegisterView(TemplateView):
    template_name = "register.html"


class ProductTable(ListView):
    template_name = 'table.html'
    model = Product
    context_object_name = "product_list"

    def get_context_data(self, **kwargs):
        context = super(ProductTable, self).get_context_data(**kwargs)
        response = requests.get("http://127.0.0.1:8000/index/api/product1")
        return context


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_class = (TokenAuthentication)
