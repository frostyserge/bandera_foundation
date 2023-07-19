"""
URL configuration for charity_org project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework_simplejwt import views as jwt_views
from django.conf import settings # this is to have access to settings.py file from here
from django.conf.urls.static import static # function that allows ut to connect with urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    # configuration for access token and refresh token
    path('token/', 
          jwt_views.TokenObtainPairView.as_view(), 
          name ='token_obtain_pair'),
     path('token/refresh/', 
          jwt_views.TokenRefreshView.as_view(), 
          name ='token_refresh'),
]

# this function connects our variables in the settings.py file and pointing to which diretory to look into
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
