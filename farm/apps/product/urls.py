from django.urls import path
from product.views import *

app_name = 'product'

urlpatterns = [
   path('', SignUpCreateView.as_view(), name='signup'),
   path('add/product/',ProductCreateView.as_view(),name='add-product'),
   path('product/list/',ProductListView.as_view(),name='product-list'),
   path('product/update/<int:pk>', ProductUpdateView.as_view(), name='product-update'),
   path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product-delete'), 
   path('product/detail/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
   path('create_bill/', CustomerDataStore.as_view(), name='create_bill'), 
   path('retrive_bill/<int:pk>/', RetriveBillData.as_view(), name='retrive_bill'), 
   path('bills/', BillList.as_view(), name='bills'), 
  ] 