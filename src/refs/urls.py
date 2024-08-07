from django.urls import path, include

from . import views 

app_name = "references"

urlpatterns = [
    path('author-list/', views.author_list, name="author-list"),
    path('author-detail/<int:author_id>/', views.author_detail, name="author-detail" ),
    path('author-update/<int:author_id>/', views.author_update, name="author-update"),
    path('author-create/', views.author_create, name="author-create"),
    path('series-list-cbv/', views.SeriesList.as_view(), name="series-list-cbv"),
    path('series-list/', views.series_list, name="series-list"),
    path('series-detail/<int:serie_id>/', views.series_detail, name="series-detail"),
    path('series-create/', views.series_create, name="series-create"),
]
# path('series-list/', views.series_list, name="series-list"),