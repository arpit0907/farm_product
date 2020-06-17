# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from django.views import View
from .models import Product, User, CustomeDetailBill 
from product.forms import ProductForm, SignUpForm, CustomerBillForm
from .helpers import subscribe_stoke_data
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

    def post(self,request):
        try:
            form = CustomerBillForm(request.POST)
            if form.is_valid():
                    subscribe_stoke_data(form)
                    commit_form = form.save(commit=False)
                    commit_form.total_list = request.POST.getlist('total_list')
                    commit_form.product_list = request.POST.getlist('product_list')
                    commit_form.quantity_list = request.POST.getlist('qty_list')
                    commit_form.unit_price_list = request.POST.getlist('unit_price_list')
                    commit_form.save()
                    return redirect('/bills/')
            return render(self.request, 'billing/product_bill.html', {'form': form})
        except Exception as e:
            return render(self.request, 'billing/product_bill.html', {'error':str(e)})
    

class RetriveBillData(View):
    def get(self,request,pk):
        customer_bills = CustomeDetailBill.objects.get(pk=pk)
        return render(self.request, 'billing/retrive_bill_list.html',{'cust_bill':customer_bills})


class BillList(View):
    def get(self,request):
        bills = CustomeDetailBill.objects.all()
        return render(self.request, 'billing/bills_list.html',{'bills':bills})


