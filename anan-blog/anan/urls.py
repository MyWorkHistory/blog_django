"""anan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from django.conf.urls import url
from base.views import commonViews

from django.views.defaults import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('articles/', include('blog.urls')),
    path('order/', include('order.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('summernote/', include('django_summernote.urls')),
    # url('ckeditor/', include('ckeditor_uploader.urls')),
    # url('crm/', include('crm.urls')),
    # url(r'^404/$', page_not_found)
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('crm/', include('crm.urls')),
    path(r'^404/$', page_not_found)

]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = commonViews.Error404
