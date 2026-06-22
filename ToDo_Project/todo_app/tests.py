from django.test import TestCase
from .models import Todo
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from django.urls import reverse
# Create your tests here.
class TodoModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='ali',password="alijamil")
    
    def test_str_returns_title(self):
        todo = Todo.objects.create(user=self.user,title='grocery')
        self.assertEqual(str(todo),'grocery')
    def test_mark_complete(self):
        todo = Todo.objects.create(user=self.user,title='task')
        result = todo.mark_complete()
        todo.refresh_from_db()
        self.assertTrue(result)
        self.assertTrue(todo.completed)
    def test_is_overdue_true_for_past_due_date(self):
        yesterday = timezone.now().date() - datetime.timedelta(days=1)
        todo = Todo.objects.create(user=self.user,title='test',due_date=yesterday)
        self.assertTrue(todo.is_overdue())

class RegisterViewTest(TestCase):
    def test_register_page_loads(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code,200)
        
        
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Todo



class RegisterViewTests(TestCase):
    def test_register_page_loads(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_register_creates_user_and_logs_in(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
        })
        self.assertTrue(User.objects.filter(username='newuser').exists())
        self.assertRedirects(response, reverse('todo_list'))

    def test_register_with_mismatched_passwords_fails(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser2',
            'password1': 'StrongPass123!',
            'password2': 'DifferentPass456!',
        })
        self.assertFalse(User.objects.filter(username='newuser2').exists())


class LogoutViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='ali', password='testpass123')

    def test_logout_post_redirects_to_login(self):
        self.client.login(username='ali', password='testpass123')
        response = self.client.post(reverse('logout'))
        self.assertRedirects(response, reverse('login'))


class TodoListViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='ali', password='testpass123')
        self.other_user = User.objects.create_user(username='irtaza', password='testpass123')
        self.my_todo = Todo.objects.create(user=self.user, title='My task')
        self.other_todo = Todo.objects.create(user=self.other_user, title='Not mine')

    def test_login_required_redirects_anonymous_user(self):
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, 302)

    def test_list_shows_only_own_todos(self):
        self.client.login(username='ali', password='testpass123')
        response = self.client.get(reverse('todo_list'))
        todos = list(response.context['todos'])
        self.assertIn(self.my_todo, todos)
        self.assertNotIn(self.other_todo, todos)