from django.urls import path

from .views import index, article, salutation

urlpatterns = [
    path('', index, name="blog-index"),
    path('salut/', salutation, name="blog-salutation"),
    path('article-<str:numero_article>/', article, name="blog-article"),
]