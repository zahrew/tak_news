from django.contrib import admin
from django.urls import path
from news.views import NewsList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/news/', NewsList.as_view(), name='news-list'),
]
