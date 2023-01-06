from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from api.serializers import AuthorSerializer, BlogSerializer
from tut.models import Author, Blog
from django.db.models import Q
from api.filters import AuthorFilter

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS, AllowAny

class AuthorDetail(APIView):
    def get(self, request, pk):
        dt = Author.objects.filter(id=pk)
        data = AuthorSerializer(dt, many=True).data
        return Response(data)

    def get_queryset(self):
        return Author.objects.filter(id=self.kwargs['pk'])
    

class AuthorList(generics.ListAPIView):
    # def get(self, request):
    #     dt = Author.objects.all()
    #     data = AuthorSerializer(dt, many=True).data
    #     return Response(data)
    model = Author
    serializer_class = AuthorSerializer
    filterset_class = AuthorFilter

    def get_queryset(self):
        queryset = Author.objects.all()
        name = self.request.query_params.get('name')
        id = self.request.query_params.get('id')
        if name and id is not None:
            # print(name)
            queryset = queryset.filter(Q(name=name)&Q(id=id))
        return queryset


class CustomList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated | BasePermission | AllowAny]


class CustomDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated | BasePermission | AllowAny]

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class PostView(APIView):
    serializer_class = BlogSerializer
    # permission_classes = []
    # authentication_classes = []
    # permission_classes = [IsAuthenticated]
    # permission_classes = [BasePermission]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated | BasePermission | AllowAny]

    def post(self, request):
        # if not self.request.session.exists(self.request.session.session_key):
        #     self.request.session.create()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            print('success')
        return Response(request.data)

    def get_queryset(self):
        return Blog.objects.all()
