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

def add_item_to_cart_view(request):
    if request.method == "POST":
        add_item_to_cart(request)
    return HttpResponseRedirect(reverse_lazy('orders:view-cart'))