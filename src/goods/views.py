from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from . import models, forms


class ItemCreate(generic.CreateView):
    model = models.Item
    fields = [
        'title', 'cover', 'price', 'author', 'series', 'genre', 
        'publishing_year', 'pages', 'binding', 'format', 'isbn',
        'weight', 'age_restrictions', 'publishing', 'item_in_stock',
        'active', 'rating'
        ]

class ItemUpdate(generic.UpdateView):
    model = models.Item
    fields = [
        'title', 'cover', 'price', 'author', 'series', 'genre', 
        'publishing_year', 'pages', 'binding', 'format', 'isbn',
        'weight', 'age_restrictions', 'publishing', 'item_in_stock',
        'active', 'rating'
        ]
    
class ItemDetail(generic.DetailView):
    model = models.Item

class ItemList(generic.ListView):
    model = models.Item

class ItemDelete(generic.DeleteView):
    model = models.Item
    success_url = reverse_lazy("goods:item-list")


def contact_form(request):
    if request.method == "GET":
        form = forms.ContactForm()
        context = {"form": form}
        return render(
        request, 
        template_name="goods/contact_form.html",
        context=context)
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            # send_email_to_manager(date)
            pass
        else:
             context = {"form": form}
             return render(
                 request, 
                 template_name="goods/contact_form.html",
                 context=context
                 )
        return HttpResponseRedirect("/mess_send")
    
    # return HttpResponseRedirect(reverse_lazy("goods:item-detail"))

# def basic_form(request):
#     if request.method == "GET":
#         form = forms.BasicForm()
#         context = {"form": form}
#         return render(
#         request, 
#         template_name="goods/basic_form.html",
#         context=context)  
