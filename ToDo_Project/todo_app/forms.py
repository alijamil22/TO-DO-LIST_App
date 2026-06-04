from django.forms import ModelForm
from .models import Todo
class Todo_Form(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'priority', 'category', 'due_date']