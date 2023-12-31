"""drf_api URL Configuration

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
from .views import root_route
from .views import root_route, logout_route
from dj_rest_auth.views import (LoginView, UserDetailsView)
from .views import CookieTokenRefreshView, CookieTokenObtainPairView

urlpatterns = [
    path('', root_route),
    path('admin/', admin.site.urls),
    # Enable logon
    path('api-auth', include('rest_framework.urls')),
    # our logout route has to be above the default one to be matched first
    path('dj-rest-auth/logout/', logout_route),
    path('dj-rest-auth/login/', LoginView.as_view(), name='rest_login'),
    path('dj-rest-auth/user/', UserDetailsView.as_view(), name='rest_user_details'),
    path('dj-rest-auth/token/', CookieTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('dj-rest-auth/token/refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),
    # # enable user registration
    path('dj_rest_auth/', include('dj_rest_auth.urls')),
    path(
        'dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')
        ),
    path('', include('profiles.urls')),
    path('', include('drawers.urls')),
    path('', include('items.urls')),
    path('', include('likes.urls')),
    path('', include('followers.urls')),
]
