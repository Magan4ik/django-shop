from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from shop.models import Category, Product


# Create your views here.

class ShopPage(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "shop/main_page.html")


class ProductsPage(View):
    def get(self, request: HttpRequest, category_slug: str) -> HttpResponse:
        if Category.objects.filter(slug=category_slug).exists():
            category = Category.objects.filter(slug=category_slug).first()
            products = category.products.all()
            return render(request, "shop/products.html", {"category": category, "products": products})
        return redirect('shop:categories')


class CategoriesPage(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        categories = Category.objects.all()
        return render(request, 'shop/categories.html', {"categories": categories})


class DetailPage(View):
    def get(self, request: HttpRequest, product_slug: str) -> HttpResponse:
        if Product.objects.filter(slug=product_slug).exists():
            product = Product.objects.filter(slug=product_slug).first()
            return render(request, 'shop/detail.html', {"product": product})
        return redirect('shop:categories')
