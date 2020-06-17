from django import template
from product.models import Product, User
from django.utils.timezone import datetime


register = template.Library()

@register.simple_tag
def get_poducts():
    product = Product.objects.all()
    return product

@register.simple_tag
def today_days():
	today = datetime.today()
	return today.strftime("%A %d/%m/%Y, %H:%M:%S")

@register.simple_tag
def filter_bill(bill_obj):
	bill_dict =[]
	qty = bill_obj.quantity_list
	for obj in range(0,len(qty)):
		bill_dict.append({
		'product_list': bill_obj.product_list[obj],
		'quantity_list': qty[obj],
		'unit_price_list': bill_obj.unit_price_list[obj],
		'total_list' : bill_obj.total_list[obj]
		})
	return bill_dict

	print(bill_dict)




		



