from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("search/", views.search_view, name="search"),
    path("delete/", views.delete_view, name="delete"),
    path("new_task/", views.new_task_view, name="new_task"),
    path("edit_task/", views.edit_task_view, name="edit_task"),
    path("filter/", views.filter_tasks_view, name="filter"),
]