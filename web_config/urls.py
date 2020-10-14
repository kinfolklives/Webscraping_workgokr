"""web_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from workgokr import views as workview
from board import views as boardview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', workview.home, name='home'),
    path("hello", workview.hello, name="hello_home"),
    path("board/listwithmongo/", boardview.listwithmongo), # add
    path("workdb", workview.workDB), # add
    path("home", workview.home),
]
