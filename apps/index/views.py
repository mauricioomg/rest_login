#from rest_framework.authentication import TokenAuthentication
#from rest_framework.permissions import IsAuthenticated
#from apps.index.serializers import UserSerializer
#from rest_framework import viewsets, permissions
from django.views.generic import TemplateView
#from django.contrib.auth.models import User
from django.shortcuts import render
import requests
#from .services import get_username

class IndexView(TemplateView):
    template_name = "index.html"


#class ProductTable(TemplateView):
  #  template_name = 'table.html'

def product_get(request):
    response = requests.get('http://127.0.0.1:8001/api/product1/')
    data = response.json()
    return render(request,'table.html',{
        'id': data,
        'fullname': data,
        'price': data,
        'detail': data

    })

    #def get_context_data(self, **kwargs):
    #    context = super(ProductTable, self).get_context_data(**kwargs)
    #    response = requests.get("http://127.0.0.1:8001/api/product1/")
    #    return context



#class UserViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows users to be viewed or edited.
#    """
#    queryset = User.objects.all().order_by('-date_joined')
#    serializer_class = UserSerializer
#    permission_classes = [permissions.IsAuthenticated]
#    authentication_class = (TokenAuthentication)
