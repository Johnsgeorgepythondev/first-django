from django.test import TestCase
from shop.models import Books

class TestModels(TestCase):
    def test_book_model(self):
        book1=Books.objects.create(name="Wings of Fire", price=1000,stock=10)
        self.assertEqual(str(book1),"Wings of Free")
        self.assertTrue(isinstance(book1,Books))