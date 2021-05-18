from django.views.generic import ListView, DetailView, TemplateView
from .models import Product


class ShopTemplateView(TemplateView):
    template_name = 'shop/index.html'


class ProductListView(ListView):
    model = Product
    template_name = 'products/index.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/details.html'
