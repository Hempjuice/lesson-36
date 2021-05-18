from django.test import TestCase
from products.models import Product


class ProductTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Test Product', price=1)

    def test_product_count(self):
        self.assertEqual(self.product.product_count(), 1)

    def test_product_name(self):
        name = self.product._meta.get_field('name').verbose_name
        self.assertEqual(name, 'name')

    def test_product_name_max_length(self):
        max_length = self.product._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_product_price(self):
        self.assertIsNotNone(self.product.price)
