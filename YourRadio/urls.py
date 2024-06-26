"""
URL configuration for YourRadio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from YourRadio import views
from . import settings

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("admin/", admin.site.urls),
    path("users/", include("django.contrib.auth.urls")),
    path("users/", include("users.urls", namespace="users")),
    path("artists/", include("artists.urls", namespace="artists")),
    path("comments/", include("comments.urls", namespace="comments")),
] + static(settings.ALBUM_MEDIA_URL, document_root=settings.ALBUM_MEDIA_ROOT)
