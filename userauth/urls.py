"""userauth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# from users.urls import user_urls
from django.conf.urls import url, include
from users import views


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^users/', views.UserListView.as_view(), name='user-list'),
    url(r'^create-user/$', views.CreateUserView.as_view(), name='create-user'),
    url(r'^update-user/(?P<pk>[a-zA-Z0-9_]+)/', views.UpdateUserView.as_view(), name='update-user'),
    url(r'^delete-user/(?P<pk>[a-zA-Z0-9_]+)/', views.DeleteUserView.as_view(), name='delete-user'),
    url(r'^activate/(?P<uid>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.AccountActivationView.as_view(), name='acount-activate')
]
