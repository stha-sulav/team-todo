from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
# Create your views here.


class TodoListCreate(generics.ListCreateAPIView):
    '''
    This view will list all the todos and create a new todo.
    '''
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    

class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    '''
    This view retrieve, update and delete a todo.
    '''
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    