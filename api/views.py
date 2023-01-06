from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from api.serializers import AuthorSerializer
from tut.models import Author
from django.db.models import Q
from api.filters import AuthorFilter


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
    pass 


class CustomDetail(generics.RetrieveDestroyAPIView):
    pass 