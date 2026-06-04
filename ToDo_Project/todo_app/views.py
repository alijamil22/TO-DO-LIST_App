from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from .models import Todo
from .forms import Todo_Form
class TodoListView(ListView):
    model = Todo
    template_name = 'todo_app/todo_list.html'
    context_object_name = 'todos'
    def get_queryset(self):
        status = self.request.GET.get('status')
        if status == 'completed':
            return Todo.objects.filter(completed=True)
        elif status == 'pending':
            return Todo.objects.filter(completed=False)
        return Todo.objects.all()
class TodoCreateView(CreateView):
    model = Todo
    template_name = 'todo_app/todo_form.html'
    form_class = Todo_Form
class TodoUpdateView(UpdateView):
    model = Todo
    template_name = 'todo_app/todo_form.html'
    form_class = Todo_Form
class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo_app/todo_confirm_delete.html'
    def get_success_url(self):
        return reverse('todo_list')