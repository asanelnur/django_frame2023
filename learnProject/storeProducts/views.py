from django.shortcuts import render

from storeProducts.models import Product, ProductCategory


# Create your views here.


def index(request):
    context = {
        'title': 'storeApp',
        'username': 'Elnur Asan',
        'is_promotion': True
    }
    return render(request, 'storeProducts/index.html', context)


def products(request):
    context = {
        'title': 'products',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'storeProducts/products.html', context)

# def products(request):
#     context = {
#         'title': 'products',
#         'products': [
#             {
#                 "title": "Худи черного цвета с монограммами adidas Originals",
#                 "price": "6 090,00",
#                 "text": "Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.",
#                 "image": "/static/vendor/img/products/Adidas-hoodie.png"
#             },
#             {
#                 "title": "Синяя куртка The North Face",
#                 "price": "23 725,00",
#                 "text": " Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.",
#                 "image": "/static/vendor/img/products/Blue-jacket-The-North-Face.png"
#             },
#             {
#                 "title": "Коричневый спортивный oversized-топ ASOS DESIGN",
#                 "price": "3 390,00",
#                 "text": " Материал с плюшевой текстурой. Удобный и мягкий.",
#                 "image": "/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png"
#             },
#             {
#                 "title": "Черный рюкзак Nike Heritage",
#                 "price": "2 340,00",
#                 "text": " Плотная ткань. Легкий материал.",
#                 "image": "/static/vendor/img/products/Black-Nike-Heritage-backpack.png"
#             },
#             {
#                 "title": "Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex",
#                 "price": "13 590,00",
#                 "text": "Гладкий кожаный верх. Натуральный материал.",
#                 "image": "/static/vendor/img/products/Black-Dr-Martens-shoes.png"
#             },
#             {
#                 "title": "Темно-синие широкие строгие брюки ASOS DESIGN",
#                 "price": "2 890,00",
#                 "text": "Легкая эластичная ткань сирсакер Фактурная ткань.",
#                 "image": "/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png"
#             },
#
#         ]
#     }
#
#     return render(request, 'storeProducts/products.html', context)
