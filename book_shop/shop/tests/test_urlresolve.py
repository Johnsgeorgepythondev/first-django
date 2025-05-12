from django.test import TestCase
from django.urls import reverse, resolve
from shop.views import home

class TestUrl(TestCase):
    def testHome(self):
        url= reverse('home')
        print("Reverse method output is",url)
        print("Resolve method output is", resolve(url))
        self.assertEqual(resolve(url).func, home)
