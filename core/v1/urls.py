from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('blog/left-sidebar/', views.blog_left_sidebar, name='blog_left_sidebar'),
    path('blog/fullwidth/', views.blog_fullwidth, name='blog_fullwidth'),
    path('blog/single/', views.blog_single, name='blog_single'),
    path('blog/single/left-sidebar/', views.blog_single_left_sidebar, name='blog_single_left_sidebar'),
    path('blog/single/fullwidth/', views.blog_single_fullwidth, name='blog_single_fullwidth'),
    path('business/', views.business, name='business'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('foods/', views.foods, name='foods'),
    path('forgot/', views.forgot, name='forgot'),
    path('lifestyle/', views.lifestyle, name='lifestyle'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register, name='register'),
    path('shop/', views.shop, name='shop'),
    path('shop/single/', views.shop_single, name='shop_single'),
    path('travels/', views.travels, name='travels'),
    path('404/', views.error_404, name='error_404'),
]
