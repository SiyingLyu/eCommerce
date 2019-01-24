
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Product

class ProductListView(ListView):
	queryset = Product.objects.all()
	template_name = "products/list.html" # product_list.html is a default name

	# def get_context_data(self, *args, **kwargs):
	# 	context = super(ProductListView, self).get_context_data(*args, **kwargs)
	# 	print(context) # see the context in the generic view (all the context passed to the view)
	# 	return context

# The following 5 lines has the same result as line 6-7
def product_list_view(request):
	queryset = Product.objects.all()
	context = {
		'object_list' : queryset # class way you cannot show the querset (set in html)
	}
	return render(request, 'products/list.html', context)


class ProductDetailView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html" 

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		print(context) # see the context in the generic view (all the context passed to the view)
		return context

def product_detail_view(request, pk=None, *args, **kwargs):
	# instance = Product.objects.get(pk=pk)
	# instance = get_object_or_404(Product, pk=pk)
	# try:
	# 	Product.objects.get(id=pk)
	# except Product.DoseNotExist:
	# 	print('no product here')
	# except:
	# 	print('Huh?')

	instance = Product.objects.get_by_id(id=pk)
	if instance == None:
		raise Http404("not exist")

	context = {
		'object' : instance # class way you cannot show the querset (set in html)
	}
	return render(request, 'products/detail.html', context)