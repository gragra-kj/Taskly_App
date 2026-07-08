
# from django.contrib import admin
# from django.conf import settings
# from django.urls import path,include
# from users import router as users_api_router
# from house import router as house_api_router
# from task import router as task_api_router
# from django.conf.urls.static import static
# from .views import api_root

# auth_api_url = [
   
# ]

# if settings.DEBUG:
#     auth_api_url.append(path('verify/', include('rest_framework.urls')))

# api_url_pattern = [
#     path('accounts/', include(users_api_router.router.urls)),
#     path('auth/', include(auth_api_url)),
#     path(r'house/',include(house_api_router.router.urls)),
#     path(r'task/',include(task_api_router.router.urls)),
# ]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/',include(api_url_pattern))
# ]
# urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from users import router as users_api_router
from house import router as house_api_router
from task import router as task_api_router

from .views import api_root

auth_api_url = []

if settings.DEBUG:
    auth_api_url.append(
        path("verify/", include("rest_framework.urls"))
    )

urlpatterns = [
    path("admin/", admin.site.urls),

    # API home
    path("api/", api_root, name="api-root"),

    # API endpoints
    path("api/accounts/", include(users_api_router.router.urls)),
    path("api/auth/", include(auth_api_url)),
    path("api/house/", include(house_api_router.router.urls)),
    path("api/task/", include(task_api_router.router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)