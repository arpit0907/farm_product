from product.models import CustomeDetailBill, Product

def subscribe_stoke_data(sub_obj):
	try:
		qty_lengh = sub_obj.data.getlist('qty_list')
		product_list = sub_obj.data.getlist('product_list')
		convert_to_dict = {}
		for lenght in range(0,len(qty_lengh)):
			get_product = Product.objects.get(name=product_list[lenght])
			qty = get_product.quantity - int(qty_lengh[lenght])
			if qty >= 0:
				get_product.quantity = qty
				get_product.prize = (get_product.prize)-float(sub_obj.data.get('total_amount'))
				get_product.save()
				convert_to_dict[product_list[lenght]] = qty_lengh[lenght]

				return True
			else:
				raise Exception("your "+product_list[lenght]+" stoke is fulled so we can not add "+product_list[lenght]+" product in the bill list")

	except Exception as e:
		raise Exception(str(e))