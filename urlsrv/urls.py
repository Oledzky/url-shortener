"""
URL configuration for urlsrv project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from shortener import views as v

urlpatterns = [

    # POST /shorten - tworzy skrócony URL
    path('shorten', v.ShortenView.as_view(), name='shorten'),

    # GET /expand/<code> - zwraca JSON z oryginalnym URL-em
    path('expand/<str:code>', v.ExpandView.as_view(), name='expand'),

    # GET /<code> - przekierowuje do oryginalnego URL-a
    path('<str:code>', v.redirect_view, name='redirect'),
]
