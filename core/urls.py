"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from apps.api import views

router = routers.DefaultRouter() # це роутер для автоматичного визначення шляхів до ресурсів
router.register(r'users', views.UserViewSet) # реєструємо ресурси users та groups
router.register(r'groups', views.GroupViewSet) #google.com/api/v1/groups/


urlpatterns = [ #google.com/
               
               
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/', include(router.urls)),#google.com/api/v1/
    path('api/v2/', include('apps.api.urls')),#google.com/api/v2/
    
    
    path('order/', include('apps.order.urls')),#google.com/order/
    path('catalog/', include('apps.catalog.urls')),#google.com/catalog/ 
    path('admin/', admin.site.urls),#google.com/admin/
    path('blog/', include('apps.blog.urls')),#google.com/blog/
    path('members/', include('apps.members.urls')),#google.com/members/
    path('', include('apps.main.urls')),#google.com/
    path("__debug__/", include("debug_toolbar.urls")),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
