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




def product_get(request):
    response = requests.get('http://127.0.0.1:8001/api/product1/')
    data = response.json()
      
    return render(request,'table.html',{
        'dataproduct': data,
       

    })

class Register(TemplateView):
    template_name = 'register.html'
    api_endpoint = "http://127.0.0.1:8001/api/users/" 
    
    


#class Login(FormView):
 #   template_name = 'login.html'
  #  form_class = AuthenticationForm
   # success_url = reverse_lazy('index:product_table')

   # @method_decorator(csrf_protect)
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
#       # logout(request)
#        return Response(status = status.HTTP_200_OK)
#    
#    #def get_context_data(self, **kwargs):
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
