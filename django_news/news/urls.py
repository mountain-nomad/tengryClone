from django.urls import path

from . import views


urlpatterns = [
    path("", views.NewsView.as_view()),
    path("filter/", views.FilterNewsView.as_view(), name='filter'),
    path("search/", views.Search.as_view(), name='search'),
    path("<slug:slug>/", views.NewDetailView.as_view(), name="new_detail"),
]