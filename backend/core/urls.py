from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CanvassListViewSet, ItemViewSet, MasterProductViewSet

router = DefaultRouter()
router.register(r'lists', CanvassListViewSet)
router.register(r'items', ItemViewSet)
router.register(r'products', MasterProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
