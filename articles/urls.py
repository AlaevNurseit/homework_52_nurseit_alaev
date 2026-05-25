from django.urls import path
from articles.views import todolist_list, todolist_create, todolist_detail

urlpatterns = [
    path("todolist/", todolist_list),
    path("todolist/add/", todolist_create),
    path("todolist/detail/", todolist_detail),
]