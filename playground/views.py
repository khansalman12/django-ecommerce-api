from django.shortcuts import render,HttpResponse
from store.models import Product


# Create your views here.
def say_hello(request):
    query_set = Product.objects.get(pk=1)
    return HttpResponse("Hello World")

