from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Review
from .forms import ProductForm, ReviewForm
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


# Product CRUD
class ProductList(ListView):
    model = Product
    template_name = 'store/product/list.html'

    def get(self, request):
        '''Shows all products available in the marketplace.'''
        products = self.get_queryset().all()
        return render(request, self.template_name, {
            'products': products
        })


class ProductCreate(LoginRequiredMixin, CreateView):
    '''Submit a form to post new product for display.'''
    model = Product
    form_class = ProductForm
    template_name = 'store/product/create.html'
    queryset = Product.objects.all()
    login_url = 'accounts:login'

    def form_valid(self, form):
        '''Initializes the passenger based on who submitted the form.'''
        form.instance.seller = self.request.user
        return super().form_valid(form)


class ProductDetail(DetailView):
    model = Product
    template_name = 'store/product/detail.html'

    def get(self, request, slug):
        """Renders a page to show the boarding instructions for a specific
           Product.

           Parameters:
           request(HttpRequest): the GET request sent to the server
           slug(str): unique slug value of the Product instance

           Returns:
           HttpResponse: the view of the detail template

        """
        product = self.get_queryset().get(slug__iexact=slug)
        context = {
            'product': product
        }
        return render(request, self.template_name, context)


class ProductUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''Allows user to update a product.'''
    model = Product
    form_class = ProductForm
    template_name = 'store/product/update.html'
    queryset = Product.objects.all()
    login_url = 'accounts:login'

    def test_func(self):
        '''Ensures the user editing the product is its seller.'''
        product = self.get_object()
        return (self.request.user == product.seller)


class ProductDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''Allows for removal of Trip instances by User.'''
    model = Product
    template_name = 'store/product/delete.html'
    success_url = reverse_lazy('store:product_list')
    login_url = 'accounts:login'
    queryset = Product.objects.all()

    def test_func(self):
        '''Ensures the user removing the product is its seller.'''
        product = self.get_object()
        return (self.request.user == product.seller)
