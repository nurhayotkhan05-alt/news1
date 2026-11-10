from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def blog(request):
    return render(request, 'blog.html')


def blog_left_sidebar(request):
    return render(request, 'blog-left-sidebar.html')


def blog_fullwidth(request):
    return render(request, 'blog-fullwidth.html')


def blog_single(request):
    return render(request, 'blog-single.html')


def blog_single_left_sidebar(request):
    return render(request, 'blog-single-left-sidebar.html')


def blog_single_fullwidth(request):
    return render(request, 'blog-single-fullwidth.html')


def business(request):
    return render(request, 'business.html')


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def contact(request):
    return render(request, 'contact.html')


def foods(request):
    return render(request, 'foods.html')


def forgot(request):
    return render(request, 'forgot.html')


def lifestyle(request):
    return render(request, 'lifestyle.html')


def login_page(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def shop(request):
    return render(request, 'shop.html')


def shop_single(request):
    return render(request, 'shop-single.html')


def travels(request):
    return render(request, 'travels.html')


def error_404(request):
    return render(request, '404.html')
