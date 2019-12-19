from django.contrib import admin
from rest_framework import routers
from django.urls import include, path
from api import views
from .views import index

router = routers.DefaultRouter()
router.register(r'mascotas', views.MascotaViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]