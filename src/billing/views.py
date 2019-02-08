from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
import stripe

STRIPE_PUB_KEY = "pk_test_0z5txCSLOwBLev347B8Dn2Qe" # front-end
stripe.api_key="sk_test_7o3qlp2H5a7jpo1e8XpqwbGJ" # back-end

def payment_method_view(request):
	next_url = None
	next_ = request.GET.get('next')
	if is_safe_url(next_, request.get_host()):
		next_url = next_
	return render(request, 'billing/payment-method.html', {"publish_key": STRIPE_PUB_KEY, "next_url": next_url})

def payment_method_createview(request):
	if request.method == "POST" and request.is_ajax():
		ptint(request.POST)
		return JsonResponse({"message": "Done"})
	return HttpResponse("error", status=401)
