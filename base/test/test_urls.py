from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from base.views import index_page


class TestUrls(SimpleTestCase):
    def test_index_page_url_resolved(self):
        url = reverse('index_page') 
        self.assertEquals(resolve(url).func, index_page)



