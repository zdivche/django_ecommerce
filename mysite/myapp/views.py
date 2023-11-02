from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

def index(request):
    items = Product.objects.all()
    context = {'items': items}
    return render(request, 'myapp/home.html', context=context)

def indexItem(request, my_id):
    item = Product.objects.get(id = my_id)
    context = {'item': item}
    return render(request, 'myapp/detail.html', context=context)



