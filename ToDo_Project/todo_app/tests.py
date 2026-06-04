from django.test import TestCase
from .models import Todo
# Create your tests here.
class Todo(TestCase):
    def setUp(self):
        Todo.objects.create()