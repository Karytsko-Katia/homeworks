from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

# # from django.views.decorators.csrf import csrf_exempt
# # from django.conf import settings (for import files?)

# from django.shortcuts import get_object_or_404, redirect
# from django.contrib import messages
# from django.db.models import ProtectedError


# from django.views import generic
# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from django.contrib.auth.mixins import UserPassesTestMixin
from goods import models as book_models
from . import models


# Create your views here.

def update_item_in_cart(key, quantity):
    item_in_cart_id = int(key.split(".")[1])
    item_in_cart = models.ItemInCart.objects.get(pk=item_in_cart_id)
    if int(quantity) == 0:
        item_in_cart.delete()
    else:
        item_in_cart.quantity = int(quantity)
        item_in_cart.save()

def get_or_create_current_cart(request):
    cart_id = request.session.get('cart_id', None)
    if request.user.is_anonymous:
        user = None
    else:
        user = request.user
    cart, created = models.Cart.objects.get_or_create(
        pk=cart_id,
        defaults={"user": user},
    )
    print("is the card was created?", created)
    print("Card ID", cart.pk)
    if created:
        request.session['cart_id'] = cart.pk
    # else:
    #     cart = models.Cart.objects.get()
    return cart


#   if not cart_id:
#         cart = models.Cart.objects.create(user = request.user)
#         request.session['cart_id'] = cart.pk
#     else:
#         cart = models.Cart.objects.get()
#     return cart_id


def create_order():
    pass



def get_current_cart(request):
    cart_id = request.session.get('cart_id', None)
    cart = models.Cart.objects.filter(pk=cart_id)
    if cart:
        cart = cart[0]
    else:
        cart = bool(cart)
    return cart

def add_item_to_cart(request):
    item_id = int(request.POST.get("item_id"))
    item = book_models.Item.objects.get(pk=item_id)
    price = item.price
    quantity = int(request.POST.get("quantity"))
    cart = get_or_create_current_cart(request)
    item_in_cart, created = models.ItemInCart.objects.get_or_create(
        cart=cart,
        item=item,
        defaults={
            "quantity": quantity,
            "price_per_item": price
            },
    )
    if not created:
        current_quality = item_in_cart.quantity
        item_in_cart.quantity = current_quality + quantity
        item_in_cart.save()




def view_cart(request):
    cart = get_current_cart(request)
    context = {'cart': cart}
    return render(
        request, 
        template_name="orders/view_cart.html", 
        context=context,
        )

def evaluate_cart(request):
    if request.method == "POST":
        print(request.POST)
        action = None
        for key, value in request.POST.items():
            if key[0:4] == "quan":
                update_item_in_cart(key, value)
            if key[0:4] == "acti":
                action = value
        if action == "update":          
            return HttpResponseRedirect(reverse_lazy('orders:view-cart'))
        create_order()
        return HttpResponseRedirect(reverse_lazy('orders:view-order-create'))



def add_item_to_cart_view(request):
    if request.method == "POST":
        add_item_to_cart(request)
    return HttpResponseRedirect(reverse_lazy('orders:view-cart'))