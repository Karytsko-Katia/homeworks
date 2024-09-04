from django.forms import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

# # from django.views.decorators.csrf import csrf_exempt
# # from django.conf import settings (for import files?)

# from django.shortcuts import get_object_or_404, redirect
# from django.contrib import messages
# from django.db.models import ProtectedError


from django.views import generic
# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from django.contrib.auth.mixins import UserPassesTestMixin
from goods import models as book_models
# from acc import models as acc_models
from acc.models import CustomerProfile
from . import models, forms


# Create your views here.

# def get_customer_date(user):
#     # phone_number = user.profile.phone_number
#     delivery_address = user.profile.delivery_address
#     # add_inform = user.profile.add_inform
#     return delivery_address


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


def create_order(request):
    cart = get_current_cart(request)
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
        return HttpResponseRedirect(reverse_lazy('orders:view-order-create'))



def add_item_to_cart_view(request):
    if request.method == "POST":
        add_item_to_cart(request)
    return HttpResponseRedirect(reverse_lazy('orders:view-cart'))

class OrderCreateView(generic.CreateView):
    model = models.Order
    form_class = forms.OrderCreateForm
    template_name = "orders/create_order.html"
    success_url = reverse_lazy('orders:created-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = get_current_cart(self.request)
        return context
    
    def get_form(self, **kwargs):
        form = super().get_form(**kwargs)
        profile = None
        if self.request.user.is_authenticated:
            try:
                profile = self.request.user.profile
            except CustomerProfile.DoesNotExist:
                profile = None
        if profile:
            form.fields["phone_number"].initial = profile.phone_number
            form.fields["delivery_address"].initial = profile.delivery_address
            form.fields["add_inform"].initial = profile.add_inform              
        return form
    


        # print(dir(form.fields['phone_number']))

    # def get_form(self, **kwargs):
    #     form = super().get_form(**kwargs)
    #     form.fields["phone_number"].initial = get_customer_date(self.request.user)
    #     form.fields["delivery_address"].initial = get_customer_date(self.request.user)
    #     form.fields["add_inform"].initial = get_customer_date(self.request.user)
    #     return form
    #     try:
        #     form.fields["phone_number"].initial = get_customer_date(self.request.user)
        #     form.fields["delivery_address"].initial = get_customer_date(self.request.user)
        #     form.fields["add_inform"].initial = get_customer_date(self.request.user)
        # except Profile.DoesNotExist:
        #     pass
        # return form



    def form_valid(self, form):
        order = form.save(commit=False)
        order.cart = get_current_cart(self.request)
        order.save()
        self.object = order
        return HttpResponseRedirect(self.get_success_url())
    

class OrderFullCreatedView(generic.TemplateView):
    template_name = "orders/created.html"

    def get(self, request, *args, **kwargs):
        if 'cart_id' in request.session:
            del request.session['cart_id']
        return super().get(request, *args, **kwargs)
    
    # context = self.get_context_data(**kwargs)
    #     return self.render_to_response(context)
