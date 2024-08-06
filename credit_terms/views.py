from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from credit_terms.serializers import Credit_termsSerializers
from about.pagination import ResultsSetPagination
from credit_terms.models import Credit_terms


class credit_termsListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = Credit_termsSerializers
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Credit_terms.objects.all().order_by('order')


@api_view(['GET'])
def credit_termsdetail(request, pk):
    credit = get_object_or_404(Credit_terms, pk=pk)
    serializer = Credit_termsSerializers(credit, context={'request': request})
    return Response(serializer.data)