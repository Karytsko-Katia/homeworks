from django.db import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model

from goods.models import Item

# Create your models here.

User = get_user_model()

class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="cards",
        blank=True,
        null=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        verbose_name='Created date'
        )
    updated = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        verbose_name='Modificate date'
        )

    def __str__(self):
        return f"Cart # {self.pk} for {self.user}"  
    @property
    def order_price(self):
        items = self.items.all()
        total_order_price = 0
        for item in items:
            total_order_price += item.price
        return total_order_price

class ItemInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.PROTECT,
        verbose_name="Cart",
        related_name="items",
    )
    item = models.ForeignKey(
        "goods.Item",
        on_delete=models.PROTECT,
        verbose_name="Item",
        related_name="items_in_cart",
    )
    quantity = models.IntegerField(
        verbose_name="Quantity",
        default=1,
    )
    price_per_item = models.DecimalField(
        verbose_name="Price per item",
        max_digits=7,
        decimal_places=2,
    )
    @property
    def price(self):
        return self.quantity * self.price_per_item

    def __str__(self):
        return f"Item {self.item.pk} in cart {self.cart.pk}, quantity {self.quantity}"