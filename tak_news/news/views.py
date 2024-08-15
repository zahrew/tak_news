from django.shortcuts import render
from rest_framework import generics
from .models import News
from .serializers import NewsSerializer
from django.http import HttpResponse
from django.template import loader
from django.test.runner import DiscoverRunner
import io
import logging
import sys
import traceback


class NewsList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_queryset(self):
        queryset= super().get_queryset()
        tags = self.request.query_params.get('tags',None) 

        if tags:
            queryset = queryset.filter(tags__name__in=tags.split(',')).distinct()
        return queryset



    def show_news(request):
        # دریافت تمام اخبار
        news_list = News.objects.all()

        # دریافت فیلتر تگ از پارامترهای GET
        tag = request.GET.get('tag', None)
        if tag:
            news_list = news_list.filter(tags__name=tag)

        return render(request, 'news_list.html', {'news_list': news_list})

    def show_test_results(request):
        try:
            with open('test_results.txt', 'r') as file:
                test_results = file.read()

            return HttpResponse(f"<pre>{test_results}</pre>")

        except Exception as e:
            # Log the exception
            error_message = f"Error occurred: {str(e)}\n\n"
            error_message += traceback.format_exc()

            return HttpResponse(error_message, status=500)

