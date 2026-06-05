from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView,UpdateView,DeleteView,FormView
from django.views import View
from django.contrib import messages
from .models import Todo
from django.shortcuts import get_object_or_404
from .forms import Todo_Form
#Authentication views
class RegisterView(FormView):
    template_name = 'auth/register.html'
    form_class = UserCreationForm
    
    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return redirect(reverse('todo_list'))
class LogoutView(View):
    def post(self,request):
        logout(request)
        return redirect(reverse('login'))
# Todo App views 
class TodoListView(LoginRequiredMixin,ListView):
    model = Todo
    template_name = 'todo_app/todo_list.html'
    context_object_name = 'todos'
    def get_queryset(self):
        status = self.request.GET.get('status')
        if status == 'completed':
            return Todo.objects.filter(user=self.request.user, completed=True)  
        elif status == 'pending':
            return Todo.objects.filter(user=self.request.user, completed=False) 
        return Todo.objects.filter(user=self.request.user)
class TodoCreateView(LoginRequiredMixin,CreateView):
    model = Todo
    template_name = 'todo_app/todo_form.html'
    form_class = Todo_Form
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Task created successfully!')
        return super().form_valid(form)
class TodoUpdateView(LoginRequiredMixin,UpdateView):
    model = Todo
    template_name = 'todo_app/todo_form.html'
    form_class = Todo_Form
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
    def form_valid(self, form):
        messages.success(self.request, 'Task updated successfully!')
        return super().form_valid(form)
class TodoDeleteView(LoginRequiredMixin,DeleteView):
    model = Todo
    template_name = 'todo_app/todo_confirm_delete.html'
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
    def get_success_url(self):
        messages.success(self.request, 'Task deleted successfully!')
        return reverse('todo_list')
class TodoToggleView(LoginRequiredMixin,View):
    def post(self,request,pk):
        todo = get_object_or_404(Todo, pk=pk, user=request.user)
        if todo.completed:
            todo.mark_incomplete()
            messages.success(request, f'"{todo.title}" marked as incomplete.')
        else:
            todo.mark_complete()
            messages.success(request, f'"{todo.title}" marked as complete.')
        return redirect(reverse('todo_list'))