from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
#from rest_framework.authentication import TokenAuthentication
#from rest_framework.permissions import IsAuthenticated
#from apps.index.serializers import UserSerializer
#from rest_framework import viewsets, permissions
from django.views.generic import TemplateView
#from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
import requests
from .forms import *
from django.urls import reverse

class IndexView(TemplateView):
   template_name = "index.html"



def product_get(request):
    headers={}
    print(request.session.get('token', False))
    if request.session.get('token',False):
        headers = {'autorization': 'Token ' + request.session.get('token',False)}
    print(headers)
    response = requests.get(
        'http://127.0.0.1:8001/api/product1/',headers=headers)
    data = response.json()  
    print(data)      
    return render(request,'table.html',{
        'dataproduct': data,
        })
     

class RegisterProduct(TemplateView):
    template_name = 'product_register.html'
    api_endpoint = "http://127.0.0.1:8001/api/product1/" 
    form_class = ProductForm
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        form = context["form"]
        errors = []
        success = False
        if form.is_valid():
            data = form.cleaned_data
            response = requests.post(self.api_endpoint, json=data)
            if response.status_code == 200 or response.status_code == 201:
                print('success')
                print ('yo me estoy ejecuntado')
                success = True
                return HttpResponseRedirect(reverse('index:product_table'))
            else:
                print('error')
                response_json = response.json()
                for error in response_json:
                    errors.append(response_json[error])
        context['errors'] = errors
        context['success'] = success
        return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class(self.request.POST or None)
        context["form"] = form
        return context
        

class Register(TemplateView):
    template_name = 'register.html'
    api_endpoint = "http://127.0.0.1:8001/api/users/" 
    form_class = UserForm

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        form = context["form"]
        errors = []
        success = False
        if form.is_valid():
            data = form.cleaned_data
            response = requests.post(self.api_endpoint, json=data)
            if response.status_code == 200 or response.status_code == 201:
                print('success')
                success = True
            else:
                print('error')
                response_json = response.json()
                for error in response_json:
                    errors.append(response_json[error])
        context['errors'] = errors
        context['success'] = success
        return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class(self.request.POST or None)
        context["form"] = form
        return context


class UpdateProduct(TemplateView):
    template_name = 'product_register.html'
    api_endpoint = "http://127.0.0.1:8001/api/product1/" 
    form_class = ProductForm
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        pk = self.kwargs.get('pk')
        ep_pk = str(pk)+"/"
        errors = []
        success = False
        response = requests.get(self.api_endpoint+ep_pk)
        print(response)
        data = response.json()
        print("soy data")
        print(data)       
        return render(request,self.template_name,{'object': data,})

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        pk = self.kwargs.get('pk')
        ep_pk = str(pk)+"/"
        form = context["form"]
        errors = []
        success = False
    
        if form.is_valid():
            data = form.cleaned_data
            print (data)
            response = requests.put(self.api_endpoint+ep_pk, json=data)
            print(response)
            
            if response.status_code == 200 or response.status_code == 201:
                print('success')
                success = True                
                return HttpResponseRedirect(reverse('index:product_table'))
            else:
                print('error')
                response_json = response.json()
                for error in response_json:
                    errors.append(response_json[error])
        context['errors'] = errors
        context['success'] = success
        return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class(self.request.POST or None)
        context["form"] = form
        return context
    

class DeleteProduct(TemplateView):
    template_name = 'delete.html'
    api_endpoint = "http://127.0.0.1:8001/api/product1/" 
    form_class = ProductForm
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        pk = self.kwargs.get('pk')
        ep_pk = str(pk)+"/"
        errors = []
        success = False
        response = requests.delete(self.api_endpoint+ep_pk)
        print(response)
        
        if response.status_code == 200 or response.status_code == 204:
            print('success')
            success = True
            return HttpResponseRedirect(reverse('index:product_table'))
        else:
            print('error')
                       
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class(self.request.POST or None)
        return context


class DetailProduct(TemplateView):
    template_name = 'detail_product.html'
    api_endpoint = "http://127.0.0.1:8001/api/product1/" 
    form_class = ProductForm
      
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        pk = self.kwargs.get('pk')
        ep_pk = str(pk)+"/"
        errors = []
        success = False
        response = requests.get(self.api_endpoint+ep_pk)
        print(response)
        
        if response.status_code == 200 or response.status_code == 201:
            print('success')
            success = True
            data = response.json()
            return render(request,self.template_name,{'object': data,})
        else:
            print('error')
    

class Login(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('index:product_table')

    @method_decorator(csrf_protect)   
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        data = {'username':form.cleaned_data['username'],
                'password': form.cleaned_data['password']}
        print (data)
        response = requests.post(
            'http://127.0.0.1:8001/api-token-auth/',json=data)
        print(response)
        print("aqui va data 2") 
        print(data)   
        response_json = response.json()
        print("aqi va response")
        print(response_json)
        if 'token' in response_json:
            self.request.session['token'] = response_json['token']
        return super(Login, self) .form_valid(form)


#def logout(request):
#    try:
#        del request.session['token']
#        print(token)
#    except KeyError:
#        print('No se ha podido borrar el token beach')
#        pass
#
#    return HttpResponseRedirect(reverse('index:login'))
    


class Logout(FormView):
    def get(self, request, format = None):
        request.data.Token.delete()
        logout(request)
        print(request)
        return Response(status = status.HTTP_200_OK)
    
    def get_context_data(self, **kwargs):
        context = super(ProductTable, self).get_context_data(**kwargs)
        response = requests.get('http://127.0.0.1:8001/api-token-auth/')
        return context
