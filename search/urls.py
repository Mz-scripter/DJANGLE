from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_page, name='search-page'),
    path('autocomplete/', views.autocomplete, name='autocomplete'),
]