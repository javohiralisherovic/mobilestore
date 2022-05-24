from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.http import HttpResponse

# Create your views here.


class HomeView(ListView):
    model=Product
    template_name = 'base.html'
    context_object_name = 'products'
    success_url ='/'

    def get_context_data(self, **kwargs):
        q = Product.objects.all()

        url_dict = self.request.GET
        if 'search-text' in url_dict and url_dict['search-text']:
            text = url_dict.get('search-text')
            q = q.filter(Q(title__icontains=text) | Q(brands__title__icontains=text) | Q(description__icontains=text))

        if 'from-price' in url_dict and url_dict['from-price']:
            from_price = int(url_dict['from-price'])
            q = q.filter(price__gte=from_price)
        
        if 'to-price' in url_dict and url_dict['to-price']:
            to_price = int(url_dict['to-price'])
            q = q.filter(price__lte=to_price)

        context = {'products': q}
        return context


class ProductView(ListView):
    model=Product
    template_name = 'product-view.html'
    context_object_name = 'product'
    success_url ='/'

    def get_queryset(self):
        return Product.objects.get(id=self.kwargs.get('id'))


class ProductsListView(ListView):
    model=Product
    template_name = 'products.html'
    context_object_name = 'products'
    success_url ='/'

    def get_context_data(self, **kwargs):
        q = Product.objects.all()

        url_dict = self.request.GET
        if 'search-text' in url_dict and url_dict['search-text']:
            text = url_dict.get('search-text')
            q = q.filter(Q(title__icontains=text) | Q(brands__title__icontains=text) | Q(description__icontains=text))

        if 'from-price' in url_dict and url_dict['from-price']:
            from_price = int(url_dict['from-price'])
            q = q.filter(price__gte=from_price)
        
        if 'to-price' in url_dict and url_dict['to-price']:
            to_price = int(url_dict['to-price'])
            q = q.filter(price__lte=to_price)

        context = {'products': q}
        return context


class ProductCreateView(CreateView):
    model = Product
    fields = ['title', 'description', 'price', 'product_date', 'brands', 'is_used', 'image']
    template_name = 'product-details.html'
    context_object_name = 'form'
    success_url = '/'


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['title', 'description', 'price', 'product_date', 'brands', 'is_used', 'image']
    template_name = 'product-details.html'
    context_object_name = 'form'
    success_url = '/'


    def get_object(self):
        print(self.request.GET.get('id'))
        return Product.objects.get(pk=self.kwargs.get('id'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = self.object.id
        return context


class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/'
    template_name = 'mobile_delete.html'

    def get_object(self):
        print(self.request.GET.get('id'))
        return Product.objects.get(pk=self.kwargs.get('id'))

    # def get_success_url(self):
    #     return reverse('product:home')


def contact(request):
    return render(request, 'contact.html')

def checkout(request):
    return render(request, 'checkout.html')

def about(request):
    return render(request, 'about.html')



class BrandListView(ListView):
    queryset = Brand.objects.order_by('id')
    model = Brand
    template_name = 'brand_view.html'
    context_object_name = 'brands'


class BrandCreateView(CreateView):
    model = Brand
    fields = ['title', 'country', 'city']
    template_name = 'brand_create.html'
    success_url = '../view/'


class BrandUpdateView(UpdateView):
    model = Brand
    fields = ['title', 'country', 'city']
    template_name = 'brand_update.html'
    success_url = '../view/'

    def get_object(self):
        print(self.request.GET.get('id'))
        return Product.objects.get(pk=self.kwargs.get('id'))


class BrandDeleteView(DeleteView):
    model = Brand
    template_name = 'brand_delete.html'
    success_url = '../view/'

    def get_object(self):
        print(self.request.GET.get('id'))
        return Product.objects.get(pk=self.kwargs.get('id'))
