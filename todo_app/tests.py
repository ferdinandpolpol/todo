
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from todo_app.models import Todo
from todo_app.views import TodoForm

class TodoTestCase(TestCase):
    url = reverse("todo")

    def setUp(self):
        model = get_user_model()
        self.user1 = model.objects.create_user(username="user1", password="user1")
        self.user2 = model.objects.create_user(username="user2", password="user2")

    def test_todo_form(self):
        response = self.client.get(self.url)
        self.assertEqual(response.context["form"].__class__, TodoForm().__class__)
    
    def test_todo_author(self):
        """ Test that created Todo's belong to user """
        self.client.post(self.url, {"author": self.user1.pk, "title": "user1_test1", "complete": False})
        self.client.post(self.url, {"author": self.user1.pk, "title": "user1_test2", "complete": False})

        for todo in Todo.objects.filter(title__contains="user1"):
            self.assertEqual(todo.author, self.user1)
