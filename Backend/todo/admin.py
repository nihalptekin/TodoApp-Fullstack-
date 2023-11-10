from django.contrib import admin


# Register your models here.
from .models import ToDoItem, TaskGroup
admin.site.register(ToDoItem),
admin.site.register(TaskGroup),