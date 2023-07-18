from django.contrib import admin
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),
    path('shop/', views.MerchList.as_view(), name = 'merch_list'),
    path('shop/<int:pk>/', views.MerchDetail.as_view(), name = 'merch_detail'),
    path('shop/<int:pk>/edit', views.MerchDetail.as_view(), name = 'merch_edit'),
    path('shop/<int:pk>/delete', views.MerchDetail.as_view(), name = 'merch_delete'),
    path('shop/new/', views.MerchCreate.as_view(), name = 'merch_create'),
    path('logout/', views.LogoutView.as_view(), name = 'logout'),
]

urlpatterns = format_suffix_patterns(urlpatterns)