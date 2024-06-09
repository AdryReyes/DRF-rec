from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'valoraciones', views.ValoracionViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]
