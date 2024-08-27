from django.urls import path, include

from . import views 

app_name = "accounts"

urlpatterns = [
    path('login', views.MyLoginView.as_view(), name="login" ),
]

#  path('login', views.logtin_view, name="login" ),
    # path('item-detail/<int:pk>/', views.ItemDetail.as_view(), name="item-detail" ),
    # path('item-list/', views.ItemList.as_view(), name="item-list"),
    # path('contact-us', views.contact_form, name="contact-us" ),