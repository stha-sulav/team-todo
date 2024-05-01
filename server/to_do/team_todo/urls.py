from django.urls import path
from .views import TodoListCreate, TodoRetrieveUpdateDestroy


urlpatterns = [
    path('todo-list', TodoListCreate.as_view(), name='todo-list-create'),
    path('todo-list/<int:pk>', TodoRetrieveUpdateDestroy.as_view(), name='todo-details'),
]
