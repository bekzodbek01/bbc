from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from about.serializers import *
from about.pagination import ResultsSetPagination


class AboutListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = AboutSerializers
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return About.objects.all().order_by('order')


@api_view(['GET'])
def Aboutdetail(request, pk):
    about = get_object_or_404(About, pk=pk)
    serializer = AboutSerializers(about, context={'request': request})
    return Response(serializer.data)


class NewsListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = NewsSerializers
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return News.objects.all().order_by('order')


@api_view(['GET'])
def Newsdetail(request, pk):
    news = get_object_or_404(News, pk=pk)
    serializer = NewsSerializers(news, context={'request': request})
    return Response(serializer.data)


class ConnectionListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = ConnectionSerializers
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Connection.objects.all().order_by('order')


@api_view(['GET'])
def Connectiondetail(request, pk):
    connection = get_object_or_404(Connection, pk=pk)
    serializer = ConnectionSerializers(connection, context={'request': request})
    return Response(serializer.data)


class ContactListView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers


@api_view(['GET'])
def Contactdetail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    serializer = ContactSerializers(contact, context={'request': request})
    return Response(serializer.data)



