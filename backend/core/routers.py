from rest_framework import routers
from . import viewsets

router_default = routers.DefaultRouter()
router_default.register(r'productos', viewsets.ProductoViewSet, basename='productos')

router_simple = routers.SimpleRouter() # No genera una ruta raíz para la API (es decir, no tiene la vista de lista de endpoints en /)
router_simple.register(r'productos-readonly', viewsets.ProductoReadOnlyViewSet, basename='productos-readonly')

urlpatterns = router_default.urls + router_simple.urls
