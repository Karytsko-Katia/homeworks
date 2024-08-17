from django.urls import path, include

from . import views 

app_name = "goods"

urlpatterns = [
    path('item-create/', views.ItemCreate.as_view(), name="item-create"),
    path('item-detail/<int:pk>/', views.ItemDetail.as_view(), name="item-detail" ),
    path('item-update/<int:pk>/', views.ItemUpdate.as_view(), name="item-update" ),
    path('item-list/', views.ItemList.as_view(), name="item-list"),
    path('item-delete/<int:pk>/', views.ItemDelete.as_view(), name="item-delete" ),
    path('contact-us', views.contact_form, name="contact-us" ),
]

#  path('author-list/', views.AuthorList.as_view(), name="author-list"),
#     path('author-detail/<int:pk>/', views.AuthorDetail.as_view(), name="author-detail" ),
#     path('author-update/<int:pk>/', views.AuthorUpdate.as_view(), name="author-update"),
#     path('author-delete/<int:pk>/', views.AuthorDelete.as_view(), name="author-delete"),
#     path('author-create/', views.AuthorCreate.as_view(), name="author-create"),