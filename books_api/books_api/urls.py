from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'))
]

schema_view = get_schema_view(
   openapi.Info(
      title="Library-Api",
      default_version='v1',
      description="Документация для приложения Library-Api",
      contact=openapi.Contact(email="exmoreandrew@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
   url(r'^swagger(?P<format>\.json|\.yaml)$',
       schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
       name='schema-swagger-ui'),
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
       name='schema-redoc'),
]