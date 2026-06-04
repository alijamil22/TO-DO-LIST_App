from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from .views import ( RegisterView,LogoutView,
    TodoListView,TodoCreateView,TodoDeleteView,TodoUpdateView,TodoToggleView)
urlpatterns = [
    # Auth app urls Patterns:
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(template_name='auth/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    
    # Todo app urls patterns:
    path('',TodoListView.as_view(),name='todo_list'),
    path('create/',TodoCreateView.as_view(),name='todo_create'),
    path('update/<int:pk>/',TodoUpdateView.as_view(),name='todo_update'),
    path('delete/<int:pk>/',TodoDeleteView.as_view(),name='todo_delete'),
    path('toggle/<int:pk>/', TodoToggleView.as_view(), name='todo_toggle'), 
]