# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from django.views import View
from .models import Product, User
from product.forms import ProductForm, SignUpForm
# Create your views here.

class SignUpCreateView(CreateView):
    model = User
    form_class = SignUpForm   
    success_url = '/product/list/'

class ProductCreateView(CreateView):

    model = Product
    form_class = ProductForm   
    success_url = '/product/list/'

    def form_valid(self, form, **kwargs):
        
        product = form.save(commit=False)
        product.save()
        return redirect(self.success_url)


class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    
  
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_form.html'
    success_url = '/product/list/'

   
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product_confirm_delete.html'
    success_url = '/product/list/'

   
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'

class CustomerDataStore(View):
    def get(self,request):
        return render(self.request,'billing/product_bill.html')