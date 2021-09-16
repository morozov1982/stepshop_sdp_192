from django.shortcuts import render, get_object_or_404

from mainapp.models import Product, ProductCategory
from basketapp.models import Basket


def products(request, pk=None):
    title = 'продукты | каталог'

    links_menu = ProductCategory.objects.all()

    products_all = Product.objects.all()
    category = {'name': 'продукты'}

    basket = []

    if pk is not None:
        products_all = Product.objects.filter(category__id=pk)
        category = get_object_or_404(ProductCategory, id=pk)


    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products_all,
        'category': category,
        'pk': pk,
        'basket': basket,
    }

    return render(request, 'mainapp/products.html', context)


def product(request, pk):
    title = 'продукт'

    links_menu = ProductCategory.objects.all()
    product_item = get_object_or_404(Product, id=pk)

    context = {
        'title': title,
        'links_menu': links_menu,
        'product': product_item,
    }

    return render(request, 'mainapp/product.html', context)
