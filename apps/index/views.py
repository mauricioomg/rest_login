#from rest_framework.authentication import TokenAuthentication
#from rest_framework.permissions import IsAuthenticated
#from apps.index.serializers import UserSerializer
#from rest_framework import viewsets, permissions
from django.views.generic import TemplateView
#from django.contrib.auth.models import User
from django.shortcuts import render
import requests
from .forms import *
#from .services import get_username

class IndexView(TemplateView):
    template_name = "index.html"


  

def product_get(request):
    response = requests.get('http://127.0.0.1:8001/api/product1/')
    data = response.json()        
    return render(request,'table.html',{
        'dataproduct': data,
        })

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

        
class Register(TemplateView):
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

    


#class Login(TemplateView):
#    template_name = 'login.html'
#    form_class = AuthenticationForm
#    success_url = reverse_lazy('index:product_table')
#
#    @method_decorator(csrf_protect)
#    @method_decorator(never_cache)
#    def dispatch(self, request, *args, **kwargs):
#        if request.user.is_authenticated:
#            return HttpResponseRedirect(self.get_success_url())
#        else:
#            return super(Login, self).dispatch(request, *args, **kwargs)
#
#    def form_valid(self, form):
#        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
#        token,_ = Token.objects.get_or_create(user = user)
#        if token:
#            login(self.request, form.get_user())
#            return super(Login, self).form_valid(form)
#            
#
#class Logout(APIView):
#    def get(self, request, format = None):
#        request.user.auth_token.delete()
#        logout(request)
#        return Response(status = status.HTTP_200_OK)
#    
#    def get_context_data(self, **kwargs):
#        context = super(ProductTable, self).get_context_data(**kwargs)
#        response = requests.get("http://127.0.0.1:8001/api/product1/")
#        return context
#
#

#class UserViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows users to be viewed or edited.
#    """
#    queryset = User.objects.all().order_by('-date_joined')
#    serializer_class = UserSerializer
#    permission_classes = [permissions.IsAuthenticated]
#    authentication_class = (TokenAuthentication)
