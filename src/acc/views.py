from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views


class MyLoginView(auth_views.LoginView):
    template_name = "acc/login.html"
    
    


#   from django.contrib.auth import authenticate, login
# def login_view(request):  
#   if request.method == "GET":
#          return_to = request.GET.get('next')
#          context = {
#              'return_to': return_to
#              }
#          return render(
#          request, 
#          template_name="acc/login_form.html",
#          context=context)
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         redirect_to = request.POST.get("next", "/")
#         user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return HttpResponseRedirect(redirect_to) 
#     else:
#         context = {
#             'error_message': 'Username or/and password are incorrect',
#             'username': username,
#             }
#         return render(
#                   request, 
#                   template_name="acc/login_form.html",
#                   context=context
#                   )
    # return HttpResponseRedirect("/mess_send")
    # # return reverse_lazy("goods:item-list")



# class ItemList(generic.ListView):
#     model = models.Item

# class ItemDelete(generic.DeleteView):
#     model = models.Item
#     success_url = reverse_lazy("goods:item-list")


# def contact_form(request):
#     if request.method == "GET":
#         form = forms.ContactForm()
#         context = {"form": form}
#         return render(
#         request, 
#         template_name="goods/contact_form.html",
#         context=context)
#     if request.method == "POST":
#         form = forms.ContactForm(request.POST)
#         if form.is_valid():
#             # send_email_to_manager(date)
#             pass
#         else:
#              context = {"form": form}
#              return render(
#                  request, 
#                  template_name="goods/contact_form.html",
#                  context=context
#                  )
#         return HttpResponseRedirect("/mess_send")
