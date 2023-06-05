from django.shortcuts import render
from django.http import HttpResponse  # this should be imported


# Create your views here.
def index(request):
    return HttpResponse("Boss Nla Shanana")


def item(request):
    return HttpResponse("This is another view")