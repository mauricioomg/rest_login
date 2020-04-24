
from django.urls import path, include
from .views import *


app_name = 'index' 
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('table/', ProductList.as_view(), name='product_table'),
    # path('table/update', UpdateList.as_view(), name='UpdateList'),
    path('register/', Register.as_view(), name = 'register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout, name='logout'),

    path('create_product/', RegisterProduct.as_view(), name = 'create_product'),
    path('update_product/<int:pk>/', UpdateProduct.as_view(), name = 'update_product'),
    path('delete_product/<int:pk>/', DeleteProduct.as_view(), name = 'delete_product'),
    path('detail_product/<int:pk>/', DetailProduct.as_view(), name = 'detail_product'),
]