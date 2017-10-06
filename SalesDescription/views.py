from django.shortcuts import render
from .models import Product, ProductImage
# Create your views here.
def home(request):
	products = Product.objects.all()
	templates = 'index.html'
	context = {'products':products}
	return render(request, templates, context)