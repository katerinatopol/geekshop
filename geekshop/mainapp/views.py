from django.shortcuts import render, get_object_or_404
<<<<<<< HEAD
=======

from basketapp.models import Basket
>>>>>>> lesson5
from mainapp.models import ProductCategory, Product


def products(request, pk=None):
<<<<<<< HEAD
    title = 'каталог'
=======
    title = 'продукты/каталог'
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
>>>>>>> lesson5

    links_menu = ProductCategory.objects.all()
    products = Product.objects.all().order_by('price')

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')
<<<<<<< HEAD
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
=======

>>>>>>> lesson5
        context = {
            'title': title,
            'links_menu': links_menu,
            'products': products,
<<<<<<< HEAD
            'category': category
        }
        return render(request, 'mainapp/products.html', context=context)

    same_products = Product.objects.all()[3:5]
=======
            'category': category,
        }
        return render(request=request, template_name='mainapp/products.html', context=context)

    same_products = Product.objects.all()[3:5]

>>>>>>> lesson5
    context = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'products': products,
<<<<<<< HEAD
=======
        'basket': basket,
>>>>>>> lesson5
    }
    return render(request=request, template_name='mainapp/products.html', context=context)