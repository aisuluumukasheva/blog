"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

from main.views import post_list, create_post, update_post, delete_post, filter_by_user,search,toggle_like
from reviews.views import CommentViewSet, post_comment

router = DefaultRouter()
router.register('comments', CommentViewSet)

"""=============================Swagger docs============================="""
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

swagger_view = get_schema_view(
    openapi.Info(
        title="Blog Api",
        default_version='v1',
        description="blog API"
    ),
    public=True
)


"""======================================================================"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/',swagger_view.with_ui('swagger', cache_timeout=0)),
    path('posts/', post_list),
    path('post-create/', create_post),
    path('post-update/<int:id>/', update_post),
    path('post-delete/<int:id>/', delete_post),
    path('post-filter/<int:u_id>', filter_by_user),
    path('post-search/',search),
    path('post-like/', toggle_like),
    path('', include(router.urls)),
    path('post_comment/<int:pk>', post_comment)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)