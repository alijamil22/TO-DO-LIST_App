from django.contrib import admin
from django.urls import path
from .views import TodoListView,TodoCreateView,TodoDeleteView,TodoUpdateView
urlpatterns = [
    path('',TodoListView.as_view(),name='todo_list'),
    path('create/',TodoCreateView.as_view(),name='todo_create'),
    path('update/<int:pk>/',TodoUpdateView.as_view(),name='todo_update'),
    path('delete/<int:pk>/',TodoDeleteView.as_view(),name='todo_delete'),
]