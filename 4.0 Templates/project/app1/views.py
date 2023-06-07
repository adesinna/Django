from django.shortcuts import render
from django.http import HttpResponse  # this should be imported
from .models import Item
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'Item_list': Item.objects.all()
    }

    return render(request, "app1/index.html", context)


def item(request):
    Item_list = Item.objects.all()
    context = {
        'Item_list': Item_list,
    }
    return render(request, 'app1/item_list.html', context)


def detail(request, id):
    Item_list = Item.objects.get(pk=id)  # get all by pk
    context = {
        'Item_list': Item_list,
    }

    return render(request, 'app1/detail.html', context)

