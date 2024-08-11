from django.shortcuts import render
from rest_framework import generics
from .models import News
from .serializers import NewsSerializer


class NewsList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_queryset(self):
        queryset= super().get_queryset()
        tags = self.request.query_params.get('tags',None) 

        if tags:
            queryset = queryset.filter(tags__name__in=tags.split(',')).distinct()
        return queryset



    
    

