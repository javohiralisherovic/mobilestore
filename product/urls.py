from django.urls import path, re_path

from product.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductsListView.as_view() , name='products'),
    path('search', ProductsListView.as_view() , name='search'),
    path('contact/', contact, name='contact'),
    path('checkout/', checkout, name='checkout'),
    path('about/', about, name='about'),
    path('search', HomeView.as_view(), name='search'),
    path('product-details/<int:id>/', ProductUpdateView.as_view()),
    path('product-view/<int:id>/', ProductView.as_view()),
    path('product/mobile-delete/<int:id>/', ProductDeleteView.as_view()),
    path('product-details/', ProductCreateView.as_view()),
    path('view/', BrandListView.as_view()),
    path('create/', BrandCreateView.as_view()),
    path('update/<int:id>/', BrandUpdateView.as_view()),
    path('delete/<int:id>/', BrandDeleteView.as_view()),
]