from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy
from . import models


class ItemCreate(generic.CreateView):
    model = models.Item
    fields = [
        'title', 'cover', 'price', 'author', 'series', 'genre', 
        'publishing_year', 'pages', 'binding', 'format', 'isbn',
        'weight', 'age_restrictions', 'publishing', 'item_in_stock',
        'active', 'rating'
        ]

