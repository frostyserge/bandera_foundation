from django.shortcuts import render, redirect
from django.http import Http404
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser
from .serializers import MerchSerializer
from .models import Merch
from rest_framework import status

# api views
class HomeView(APIView):
    permission_classes = [AllowAny,]

    def get(self, request):
        content = {'message': 'Welcome to our Foundation Page!'}
        return Response(content)
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        
        except Exception as e:
            return Response(status=status.status.HTTP_400_BAD_REQUEST)

class MerchList(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = Merch.objects.all()
    serializer_class = MerchSerializer
    

class MerchView(CreateAPIView):
    queryset = Merch.objects.all()
    serializer_class = MerchSerializer
    success_url = '/shop/'

class MerchDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Merch.objects.get(pk=pk)
        except Merch.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        merch_item = self.get_object(pk)
        serializer = MerchSerializer(merch_item)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        permission_classes = [IsAdminUser,]
        merch_item = self.get_object(pk)
        serializer = MerchSerializer(merch_item, data=request.data)
        if serializer.is_valid() and permission_classes == IsAdminUser:
            serializer.save()
            return Response(serializer.data) and redirect('merch_detail', pk=pk)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        merch_item = self.get_object(pk)
        merch_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) and redirect('shop', pk=pk)
