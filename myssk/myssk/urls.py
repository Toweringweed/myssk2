"""myssk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from skyuser import views as skyuser_view
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    url(r'^accounts/', include('users.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^skyuser/user_center', skyuser_view.user_center, name='user_center'),
    url(r'^skyuser/user_map', skyuser_view.user_map, name='user_map'),
    url(r'^skyuser/user_info', skyuser_view.user_info, name='user_info'),
    url(r'^skyuser/data_apply', skyuser_view.data_apply, name='data_apply'),
    url(r'^skyuser/apply_list', skyuser_view.apply_list, name='apply_list'),
    url(r'^skyuser/apply_edit/(\d+)/$', skyuser_view.apply_edit, name='apply_edit'),
    url(r'^skyuser/apply_del/(\d+)/$', skyuser_view.apply_del, name='apply_del'),
    url(r'^skyuser/file_down/(\w+)/$', skyuser_view.file_down, name='file_down'),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
]


