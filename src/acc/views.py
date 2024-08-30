from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from . import models, forms

class MyLoginView(auth_views.LoginView):
    template_name = "acc/login.html"

class CheckProfileMixin(LoginRequiredMixin):
    redirect_on_missing_profile = True
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        user = self.request.user
        profile = models.CustomerProfile.objects.filter(
            user__pk=user.pk
        )
        redirect_needed = bool(profile)
        if self.redirect_on_missing_profile == True:
            redirect_needed = not redirect_needed
        if redirect_needed:
            return HttpResponseRedirect(self.profile_redirect_url)
        return super().dispatch(request, *args, **kwargs)
    
    




class CustomerProfileCreate(CheckProfileMixin, generic.CreateView):
    profile_redirect_url = reverse_lazy('accounts:profile-detail')
    redirect_on_missing_profile = False
    model = models.CustomerProfile
    template_name = "acc/profile_create.html"
    form_class = forms.ProfileCreateForm
    success_url = reverse_lazy('accounts:profile-detail')
    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        self.object = profile
        return HttpResponseRedirect(self.get_success_url())
        


# if request.method == "GET":
#         form = forms.ContactForm()def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        profile = models.CustomerProfile.objects.filter(
            user__pk=user.pk
        )
        if not profile:
            return HttpResponseRedirect(reverse_lazy('accounts:profile-create'))
        return super().dispatch(request, *args, **kwargs)
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



    
class CustomerProfileDetail(CheckProfileMixin, generic.DetailView):
    profile_redirect_url = reverse_lazy('accounts:profile-create')
    redirect_on_missing_profile = True
    template_name = "acc/profile.html"
    def get_object(self):
        user = self.request.user
        profile = models.CustomerProfile.objects.filter(
            user__pk=user.pk
        )
        if profile:
            profile=profile[0]
        else:
            profile = models.CustomerProfile.objects.create(
                user = user,
                delivery_address = "pls fill out the form",
                phone_number = "+375(xx)xxxxxx",
                add_inform = "-"
            )
        return profile
    
# def dispatch(self, request, *args, **kwargs):
#         user = self.request.user
#         profile = models.CustomerProfile.objects.filter(
#             user__pk=user.pk
#         )
#         if not profile:
#             return HttpResponseRedirect(reverse_lazy('accounts:profile-create'))
#         return super().dispatch(request, *args, **kwargs)

# class CustomerProfileDetail(LoginRequiredMixin, generic.DetailView):
    # template_name = "acc/profile.html"
    # def get_object(self):
    #     user = self.request.user
    #     try:
    #         print(user.profile)
    #         profile = user.profile
    #     except:
    #         profile = models.CustomerProfile.objects.create(
    #             user = user,
    #             delivery_address = "pls fill out the form",
    #             phone_number = "pls fill out your phone number",
    #             add_inform = "-"
    #         )
    #     return profile

    # def get_object(self, queryset):
    #     return super().get_object(queryset)

# from django.contrib.auth import authenticate, login
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
