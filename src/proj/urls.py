"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from refs import views as refs_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('author-list/', refs_views.author_list),
    path('author-detail/<int:author_id>/', refs_views.author_detail),
    path('author-update/<int:author_id>/', refs_views.author_update),
    path('author-create/', refs_views.author_create),
    path('series-list/', refs_views.series_list),
    path('series-detail/<int:serie_id>/', refs_views.series_detail),
    path('series-create/', refs_views.series_create),
]
