from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from .serializers import MerchSerializer
from .models import Merch
from rest_framework import status

# api views
class HomeView(APIView):
    permission_classes = (AllowAny,)

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

class MerchList(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Merch.objects.all()
    serializer_class = MerchSerializer
    

# class MerchView(CreateAPIView):
#     queryset = Merch.objects.all()
#     serializer_class = MerchSerializer

class MerchDetail(RetrieveUpdateDestroyAPIView):
    queryset = Merch.objects.all()
    serializer_class = MerchSerializer
