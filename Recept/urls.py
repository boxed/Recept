"""Recept URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index),

    url(r'^recipes/$', views.recipe_list),
    url(r'^recipes/create/$', views.create_recipe),
    url(r'^recipes/(?P<pk>\d+)/edit/$', views.edit_recipe),

    url(r'^history/$', views.history),
    url(r'^history/(?P<pk>\d+)/edit/$', views.edit_plan),
    url(r'^history/plan/$', views.plan),

    url(r'^admin/', admin.site.urls),
]
