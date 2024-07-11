from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from api.views import UserViewSet

router = DefaultRouter()

router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('schema/', SpectacularAPIView.as_view(), name="schema"),
    path('docs/', SpectacularSwaggerView.as_view(url_name="schema"),
         name="docs"),
]
