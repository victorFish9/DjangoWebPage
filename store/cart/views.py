from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.
from .cart import Cart
from item.models import Item

def add_to_cart(request, item_id):
    cart = Cart(request)
    cart.add(item_id)

    return render(request, 'cart/partials/menu_cart.html')

def cart(request):
    return render(request, 'cart/cart.html')

def update_cart(request, item_id, action):
    cart = Cart(request)

    if action == 'increment':
        cart.add(item_id, 1, True)
    else:
        cart.add(item_id, -1, True)

    item = Item.objects.get(pk=item_id)
    quantity = cart.get_item(item_id)['quantity']


    item = {
        'item': {
            'id': item.id,
            'name' : item.name,
            'image': item.image,
            'get_thumbnail': item.get_thumbnail(),
            'price' : item.price,
        },
        'total_price':(quantity * item.price) / 1,
        'quantity' : quantity,
    }

    response = render(request, 'cart/partials/cart_item.html', {'item': item})

    response['HX-Trigger'] = 'update-menu-cart'

    return response

@login_required
def checkout(request):
    return render(request, 'cart/checkout.html')

def hx_menu_cart(request):
    return render(request, 'cart/partials/menu_cart.html')