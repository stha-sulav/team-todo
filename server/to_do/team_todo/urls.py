from django.urls import path
from .views import TodoListCreate, TodoRetrieveUpdateDestroy


urlpatterns = [
    path('', TodoListCreate.as_view(), name='todos'),
    path('todos/<int:pk>/', TodoRetrieveUpdateDestroy.as_view(), name='todo'),
]
