"""jetbov URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path
from django.conf.urls import include, url

from Fazenda.views import home
from Fazenda.api.views import (
	FazendaListAPI, 
	ProprietarioListAPI,
	FazendaDetailAPI,
	ProprietarioDetailAPI,
	FazendaDestroyAPI,
	FazendaUpdateAPI,
	FazendaCreateAPI,
	)

urlpatterns = [
	path('', home, name='cliente_home'),
    path('admin/', admin.site.urls),
    path('api/Fazenda/', FazendaListAPI.as_view(), name='Fazenda-api-list'),
    path('api/Fazenda/create', FazendaCreateAPI.as_view(), name='Fazenda-api-create'),
    path('api/Proprietario/', ProprietarioListAPI.as_view(), name='Proprietario-api-list'),
    re_path(r'^api/Fazenda/(?P<token>\d+)/$', FazendaDetailAPI.as_view(), name='Fazenda-api-detail'),
    re_path(r'^api/Fazenda/edit/(?P<token>\d+)/$', FazendaUpdateAPI.as_view(), name='Fazenda-api-edit'),
    re_path(r'^api/Fazenda/delete/(?P<token>\d+)/$', FazendaDestroyAPI.as_view(), name='Fazenda-api-delete'),
    # path('api/Proprietario/', ProprietarioListAPI.as_view(), name='Proprietario-api'),
]
