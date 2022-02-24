from django.contrib import admin
from django.urls import include, path, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

from userAPI.views import *

router = routers.SimpleRouter()
router.register(r'users', AdminAPI, basename='admin')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include('userAPI.urls'), name='homepage'),
    path('', include('rest_framework.urls')),
    re_path(r'auth/', include('djoser.urls.authtoken')),

    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            template_name="swagger-ui.html", url_name="schema"
        ),
        name="swagger-ui",
    ),
    path('users/', UserAPIList.as_view(), name='users'),
    path('users/current/', UserCurrentAPI.as_view()),
    path('users/<int:pk>/', UserAPIUpdate.as_view()),

    path('private/', include(router.urls)),
]
