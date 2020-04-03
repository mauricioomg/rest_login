from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
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
        response = requests.get("http://127.0.0.1:8000/api/product1/")
        print(response.json())
        return context



class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

    
class Login(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('index:product_table')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
        token,_ = Token.objects.get_or_create(user = user)
        if token:
            login(self.request, form.get_user())
            return super(Login, self).form_valid(form)
            

class Logout(APIView):
    def get(self, request, format = None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status = status.HTTP_200_OK)
        success_url = reverse_lazy('login.html')