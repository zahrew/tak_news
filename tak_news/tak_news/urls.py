from django.contrib import admin
from django.urls import path
from news.views import NewsList
from news import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/news/', NewsList.as_view(), name='news-list'),
    path('show-news/', NewsList.show_news, name='show-news'),
    path('show-test-results/', NewsList.show_test_results, name='show-test-results'),
]
