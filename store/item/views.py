from django.shortcuts import render, get_object_or_404
from .models import Item


def item(request, slug):
    item = get_object_or_404(Item, slug=slug)
    return render(request, 'item/item.html', {'item':item})