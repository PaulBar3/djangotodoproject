from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Todo_item


def index_view(request: HttpRequest) -> HttpResponse:
    todo_items = Todo_item.objects.all()
    return render(
        request,
        template_name="todo_list/index.html",
        context={"todo_items": todo_items},
    )


class Todo_List_Index_View(ListView):
    template_name = "todo_list/index.html"

    def get_content_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_items"] = Todo_item.objects.all()
        return context


class Todo_List_View(ListView):
    template_name = "todo_list/todoitem_list.html"
    model = Todo_item
    context_object_name = "todo_items"
