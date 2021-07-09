from django.shortcuts import render, get_object_or_404
from mainapp.models import ProductCategory, Product


def products(request, pk=None):
    title = 'каталог'

    links_menu = ProductCategory.objects.all()
    products = Product.objects.all().order_by('price')

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')
    # links_menu = [
    #     {'href': i.link, 'name': i.name}
    #     for i in ProductCategory.objects.all()]
    # links_menu = [
    #     {'href': 'products_all', 'name': 'все'},
    #     {'href': 'products_home', 'name': 'дом'},
    #     {'href': 'products_office', 'name': 'офис'},
    #     {'href': 'products_modern', 'name': 'модерн'},
    #     {'href': 'products_classic', 'name': 'классика'},
    # ]
        context = {
            'title': title,
            'links_menu': links_menu,
            'products': products,
            'category': category
        }
        return render(request, 'mainapp/products.html', context=context)

    same_products = Product.objects.all()[3:5]
    context = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'products': products,
    }
    return render(request, 'mainapp/products.html', context=context)
