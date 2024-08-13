from django.urls import path, include

from . import views 

app_name = "references"

urlpatterns = [
    path('author-list/', views.AuthorList.as_view(), name="author-list"),
    path('author-detail/<int:pk>/', views.AuthorDetail.as_view(), name="author-detail" ),
    path('author-update/<int:pk>/', views.AuthorUpdate.as_view(), name="author-update"),
    path('author-delete/<int:pk>/', views.AuthorDelete.as_view(), name="author-delete"),
    path('author-create/', views.AuthorCreate.as_view(), name="author-create"),
    path('series-list/', views.SeriesList.as_view(), name="series-list"),
    path('series-detail/<int:pk>/', views.SeriesDetail.as_view(), name="series-detail"),
    path('series-update/<int:pk>/', views.SeriesUpdate.as_view(), name="series-update"),
    path('series-create/', views.SeriesCreate.as_view(), name="series-create"),
    path('series-delete/<int:pk>/', views.SeriesDelete.as_view(), name="series-delete"),
    path('genre-list/', views.GenreList.as_view(), name="genre-list"),
    path('genre-detail/<int:pk>/', views.GenreDetail.as_view(), name="genre-detail"),
    path('genre-update/<int:pk>/', views.GenreUpdate.as_view(), name="genre-update"),
    path('genre-delete/<int:pk>/', views.GenreDelete.as_view(), name="genre-delete"),
    path('genre-create/', views.GenreCreate.as_view(), name="genre-create"),
    path('publishing-list/', views.PublishingList.as_view(), name="publishing-list"),
    path('publishing-create/', views.PublishingCreate.as_view(), name="publishing-create"),
    path('publishing-detail/<int:pk>/', views.PublishingDetail.as_view(), name="publishing-detail"),
    path('publishing-update/<int:pk>/', views.PublishingUpdate.as_view(), name="publishing-update"),
    path('publishing-delete/<int:pk>/', views.PublishingDelete.as_view(), name="publishing-delete"),
    path('seriesprivately-list/', views.SeriesPrivatelyList.as_view(), name="seriesprivately-list"),
    path('seriesprivately-detail/<int:pk>/', views.SeriesPrivatelyDetail.as_view(), name="seriesprivately-detail"),
    path('seriesprivately-update/<int:pk>/', views.SeriesPrivatelyUpdate.as_view(), name="seriesprivately-update"),
    path('seriesprivately-delete/<int:pk>/', views.SeriesPrivatelyDelete.as_view(), name="seriesprivately-delete"),
    path('seriesprivately-create/', views.SeriesPrivatelyCreate.as_view(), name="seriesprivately-create"),
]
# path('series-list/', views.series_list, name="series-list"),
# path('author-list/', views.author_list, name="author-list")
# path('series-detail/<int:serie_id>/', views.series_detail, name="series-detail"),
# path('author-detail/<int:author_id>/', views.author_detail, name="author-detail" ),
# path('series-create/', views.series_create, name="series-create"),
# path('author-create/', views.author_create, name="author-create"),
# path('author-update/<int:author_id>/', views.author_update, name="author-update"),