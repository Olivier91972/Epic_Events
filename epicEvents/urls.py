from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from API.views import ClientViewSet, ContractViewSet, EventViewSet, UserViewSet

from django.urls import path


def trigger_error(request):
    division_by_zero = 1 / 0


routers = routers.SimpleRouter()
routers.register('clients', ClientViewSet, basename='clients')
routers.register('contracts', ContractViewSet, basename='contracts')
routers.register('events', EventViewSet, basename='events')
routers.register('users', UserViewSet, basename='users')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(routers.urls)),
    path('sentry-debug/', trigger_error),
    ]
