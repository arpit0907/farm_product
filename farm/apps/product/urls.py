from django.urls import path
from product.views import *

app_name = 'product'

urlpatterns = [
   path('add/product/',ProductCreateView.as_view(),name='add-product'),
   path('product/list/',ProductListView.as_view(),name='product-list'),
   path('product/update/<int:pk>', ProductUpdateView.as_view(), name='product-update'),
   path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product-delete'), 
   path('product/detail/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
   path('signup/', SignUpCreateView.as_view(), name='signup'),
  ] 