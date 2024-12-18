"""
URL configuration for IFilms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

from films.views import index, film_page, favourite, search_page, toggle_favourite

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('film/<int:film_id>/', film_page, name='film_page'),
    path('film/<int:film_id>/toggle_favourite/', toggle_favourite, name='toggle_favourite'),
    path('favourite/', favourite, name='favourite'),
    path('search/', search_page, name='search'),
    path('users/', include('users.urls', namespace='users')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
