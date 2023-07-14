from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),
    path('shop/', views.MerchList.as_view(), name = 'shop'),
    path('shop/<int:pk>/', views.MerchDetail.as_view(), name = 'merch_detail'),
    path('logout/', views.LogoutView.as_view(), name = 'logout'),
]