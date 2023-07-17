from django.shortcuts import render, redirect
from django.http import Http404
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser
from .serializers import MerchSerializer
from .models import Merch
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

# api views
class HomeView(APIView):
    permission_classes = [AllowAny,]

    def get(self, request):
        content = {'message': 'Welcome to our Foundation Page!'}
        return Response(content)
    
# class UserList(APIView):
#     """
#     Create a new user. It's called 'UserList' because normally we'd have a get
#     method here too, for retrieving a list of all User objects.
#     """

#     permission_classes = [AllowAny,]
#     http_method_names = ['get', 'head']


#     def get(self, request, format=None):
#         users = User.objects.all()
#         serializer = UserSerializerWithToken(users, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         self.http_method_names.append("GET")

#         serializer = UserSerializerWithToken(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class MerchList(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = Merch.objects.all()
    serializer_class = MerchSerializer
    

class MerchCreate(CreateAPIView):
    permission_classes = [IsAuthenticated,]
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
