from django.shortcuts import render


def cart_home(request):
	cart_id = request.session.get("cart_id", None)
	if cart_id is None: # and ininstance(cart_id, int):
		print('create a new cart')
		request.session['cart_id'] = 12
	else:
		print('Cart ID exists, this is existing')
	return render(request, "carts/home.html", {})