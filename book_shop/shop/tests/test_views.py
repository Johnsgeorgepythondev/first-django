from django.test import TestCase,Client
from django.urls import reverse,resolve
from shop.models import Books

class TestViews(TestCase):
    def test_home_View(self):
        client=Client()
        response=client.get(reverse('home'))
        print("Response is: ", response)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'home.html')