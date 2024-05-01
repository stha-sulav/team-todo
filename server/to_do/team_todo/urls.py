from django.urls import path
from .views import TodoListCreate, TodoRetrieveUpdateDestroy


urlpatterns = [
    path('todo-list', TodoListCreate.as_view(), name='todo-list-create'),
    path('todos/<int:pk>', TodoRetrieveUpdateDestroy.as_view(), name='todo-details'),
]
