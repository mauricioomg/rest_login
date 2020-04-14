from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .views import product_get,Login
#from .router import router
from . import views

app_name = 'index' 
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('table/', product_get, name='product_table'),
    path('login/',  Login.as_view(), name='login' ),
    #path('api/', include(router.urls)),
]