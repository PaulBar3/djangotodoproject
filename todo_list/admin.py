from django.contrib import admin

from todo_list.models import Todo_item

@admin.register(Todo_item)
class TodoItemAdmin(admin.ModelAdmin): 
    list_display = ('title', 'done')