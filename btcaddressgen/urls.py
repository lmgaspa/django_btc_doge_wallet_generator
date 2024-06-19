from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include
from .views import ExampleAPIView
from .views import BitcoinAddressAPIView

schema_view = get_schema_view(
    openapi.Info(
        title="Bitcoin Address Generator",
        default_version='v1',
        description="a Bitcoin Address Generator",
        terms_of_service="https://www.dianaglobal.com.br/policies/terms/",
        contact=openapi.Contact(email="luhmgasparetto@gmail.com"),
        license=openapi.License(name="Diana Global License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('', include('btcaddressgenerator.urls')),
    path('btcaddressgenerator/', include('btcaddressgenerator.urls')),
    path('example/', ExampleAPIView.as_view(), name='example-api'),
    path('bitcoin/address/', BitcoinAddressAPIView.as_view(), name='bitcoin-address'),
]