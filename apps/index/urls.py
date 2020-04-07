from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .views import ProductTable
#from .router import router
from . import views

app_name = 'index' 
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('table/', login_required(ProductTable.as_view()), name='product_table'),
    #path('api/', include(router.urls)),
]