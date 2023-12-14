from django.test import  TestCase, Client
from django.urls import reverse
from .views import index_page




class TestViews(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.index_url = reverse(index_page)

    def test_index_page_GET(self):
        response = self.client.get(self.index_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/index.html')