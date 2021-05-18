from django.test import TestCase
from django.urls import reverse
from products.models import Product


class MainPageTest(TestCase):
    def test_main_page_url_exists_at_desired_location(self):
        response = self.client.get(reverse('main-page'))
        self.assertEqual(response.status_code, 200)

    def test_main_page_uses_correct_template(self):
        response = self.client.get(reverse('main-page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/index.html')


class ProductListViewTest(TestCase):
    def test_list_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('products-list'))
        self.assertEqual(response.status_code, 200)

    def test_list_view_uses_correct_template(self):
        response = self.client.get(reverse('products-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/index.html')


class ProductDetailViewTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Test Product', price=1)

    def test_detail_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('product-detail', args=[self.product.pk]))
        self.assertEqual(response.status_code, 200)

    def test_detail_view_uses_correct_template(self):
        response = self.client.get(reverse('product-detail', args=[self.product.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/details.html')

    def test_detail_view_context(self):
        response = self.client.get(reverse('product-detail', args=[self.product.pk]))
        self.assertIn('object', response.context)
        self.assertEqual(response.context['object'].name, 'Test Product')
