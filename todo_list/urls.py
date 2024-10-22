"""todo_list URL Configuration"""

from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "todo_list"


urlpatterns = [
    path("", views.index_view, name="index"),
    #path("todo_list/", views.Todo_List_Index_View.as_view(), name="todo_list"),
    path("list/", views.Todo_List_View.as_view(), name="list"),

]
