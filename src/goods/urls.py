from django.urls import path, include

from . import views 

app_name = "goods"

urlpatterns = [
    path('item-create/', views.ItemCreate.as_view(), name="item-create"),
]

#  path('author-list/', views.AuthorList.as_view(), name="author-list"),
#     path('author-detail/<int:pk>/', views.AuthorDetail.as_view(), name="author-detail" ),
#     path('author-update/<int:pk>/', views.AuthorUpdate.as_view(), name="author-update"),
#     path('author-delete/<int:pk>/', views.AuthorDelete.as_view(), name="author-delete"),
#     path('author-create/', views.AuthorCreate.as_view(), name="author-create"),