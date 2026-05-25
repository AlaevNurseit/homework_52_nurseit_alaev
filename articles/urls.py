from django.urls import path

from articles.views import articles, article_create_view, article

urlpatterns = [
    path("todolist/", articles),
    path("todolist/add/", article_create_view),
    path("todolist/detail/", article),
]