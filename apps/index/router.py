from api.viewsets import Product1Viewset
from rest_framework import routers
from apps.index import views

router = routers.DefaultRouter()
router.register('product1', Product1Viewset)
router.register(r'users', views.UserViewSet)

#