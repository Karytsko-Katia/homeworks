from django.urls import path, include

from . import views 

app_name = "references"

urlpatterns = [
    path('author-list/', views.AuthorList.as_view(), name="author-list"),
    path('author-detail/<int:pk>/', views.AuthorDetail.as_view(), name="author-detail" ),
    path('author-update/<int:author_id>/', views.author_update, name="author-update"),
    path('author-create/', views.author_create, name="author-create"),
    path('series-list/', views.SeriesList.as_view(), name="series-list"),
    path('series-detail/<int:pk>/', views.SeriesDetail.as_view(), name="series-detail"),
    path('series-create/', views.series_create, name="series-create"),
    path('genre-list/', views.GenreList.as_view(), name="genre-list"),
    path('genre-detail/<int:pk>/', views.GenreDetail.as_view(), name="genre-detail" ),
    path('publishing-list/', views.PublishingList.as_view(), name="publishing-list"),
    path('publishing-detail/<int:pk>/', views.PublishingDetail.as_view(), name="publishing-detail" ),
    path('seriesprivately-list/', views.SeriesPrivatelyList.as_view(), name="seriesprivately-list"),
    path('seriesprivately-detail/<int:pk>/', views.SeriesPrivatelyDetail.as_view(), name="seriesprivately-detail"),
]
# path('series-list/', views.series_list, name="series-list"),
# path('author-list/', views.author_list, name="author-list")
# path('series-detail/<int:serie_id>/', views.series_detail, name="series-detail"),
# path('author-detail/<int:author_id>/', views.author_detail, name="author-detail" ),