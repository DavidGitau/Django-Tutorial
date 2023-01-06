from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from api.serializers import *
from tut.models import Author


class AuthorDetail(APIView):
    id = 1

    def get(self, request, slug):
        self.id = slug
        dt = Author.objects.filter(id=self.id)
        data = AuthorSerializer(dt, many=True).data
        return Response(data)

    def get_queryset(self):
        return Author.objects.filter(id=self.id)
    

class AuthorList(APIView):
    def get(self, request):
        dt = Author.objects.all()
        data = AuthorSerializer(dt, many=True).data
        return Response(data)

    def get_queryset(self):
        return Author.objects.all()


class CustomList(generics.ListCreateAPIView):
    pass 


class CustomDetail(generics.RetrieveDestroyAPIView):
    pass 