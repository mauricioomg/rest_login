from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .views import product_get
#from .router import router
from . import views

app_name = 'index' 
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('table/', product_get, name='product_table'),
    #path('api/', include(router.urls)),
]