from django.shortcuts import render
from mainapp.models import ProductCategory


def products(request):
    title = 'каталог'
    links_menu = [
        {'href': i.link, 'name': i.name}
        for i in ProductCategory.objects.all()]
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
    }
    return render(request, 'mainapp/products.html', context=context)
