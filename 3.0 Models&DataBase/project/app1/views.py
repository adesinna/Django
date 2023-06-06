from django.shortcuts import render
from django.http import HttpResponse  # this should be imported
from .models import Item


# Create your views here.
def index(request):
    return HttpResponse("Boss Nla Shanana")


def item(request):
    item_list = Item.objects.all()
    return HttpResponse(item_list)