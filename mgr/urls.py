"""mgr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from web import views
from django.conf import settings
from django.conf.urls.static import static

poll2_words = ["kurwa", "chuj", "idiota", "debil", "szmata", "pizda", "skurwysyn", "dziwka", "kutas"]

urlpatterns = [
    path('', views.index, name='index'),
    path('intro', views.intro, name='intro'),
    path('sum_up', views.sum_up, name='sum_up'),
    path('poll1', views.first_poll, name='poll1'),
    path('poll2', views.second_poll, name='poll2'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
([path(word, getattr(views, word), name=word) for word in poll2_words])
