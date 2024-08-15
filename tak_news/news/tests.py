import os
import django
from django.conf import settings

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tak_news.settings')

# Initialize Django
django.setup()

from django.test import TestCase
from .models import News, Tag
from rest_framework.test import APIClient

class NewsAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        tag1 = Tag.objects.create(name="Tech")
        tag2 = Tag.objects.create(name="Health")
        news1 = News.objects.create(title="Tech News", body="Some tech news", source="TechSource")
        news1.tags.add(tag1)
        news2 = News.objects.create(title="Health News", body="Some health news", source="HealthSource")
        news2.tags.add(tag2)

    def test_get_news_list(self):
        response = self.client.get('/api/news/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_filter_news_by_tags(self):
        response = self.client.get('/api/news/', {'tags': 'Tech'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Tech News")

