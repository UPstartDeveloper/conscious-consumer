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
    pass


class ProductCreate(LoginRequiredMixin, CreateView):
    pass


class ProductDetail(DetailView):
    pass


class ProductUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    pass


class ProductDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    pass
