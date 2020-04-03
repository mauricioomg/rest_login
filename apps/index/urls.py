from django.urls import path, include
from . import views
from .views import ProductList, ProductTable
from .router import router

app_name = 'index'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    #path('product/', ProductList.as_view(), name='product_list'),
    path('table/', ProductTable.as_view(), name='product_table'),
    path('api/', include(router.urls))
]