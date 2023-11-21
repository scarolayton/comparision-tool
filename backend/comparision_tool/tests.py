
from django.test import TestCase
from .models import CustomUser, SavedQueries, Comments
from django.utils import timezone
from rest_framework.test import APITestCase
from .serializer import SavedQueriesSerializer, CommentsSerializer, CustomUserSerializer
from django.urls import reverse
# for the models
class CustomUserTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username="testuser")

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")

class SavedQueriesTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username="testuser")
        self.query = SavedQueries.objects.create(
            user=self.user,
            query_name="Test Query",
            query_description="Test Description",
            first_country="Colombia",
            first_date=timezone.now(),
            query_quantity=1
        )

    def test_query_creation(self):
        self.assertEqual(self.query.query_name, "Test Query")
        self.assertEqual(self.query.query_description, "Test Description")
        self.assertEqual(self.query.first_country, "Colombia")
        self.assertEqual(self.query.query_quantity, 1)

class CommentsTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username="testuser")
        self.query = SavedQueries.objects.create(
            user=self.user,
            query_name="Test Query",
            query_description="Test Description",
            first_country="Colombia",
            first_date=timezone.now(),
            query_quantity=1
        )
        self.comment = Comments.objects.create(
            author=self.user,
            text="Test Comment",
            saved_query_reference=self.query
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.text, "Test Comment")


class CustomUserViewTestCase(APITestCase):
    def test_create_user(self):
        url = reverse('customuser-list')
        data = {'username': 'testuser'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

class SavedQueriesViewTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username="testuser")
        self.query = SavedQueries.objects.create(
            user=self.user,
            query_name="Test Query",
            query_description="Test Description",
            first_country="Colombia",
            first_date="2023-11-22",
            query_quantity=1
        )

    def test_queries_by_user(self):
        url = reverse('savedqueries-queries_by_user')
        response = self.client.get(url, {'user_id': self.user.id})
        self.assertEqual(response.status_code, 200)

    def test_create_saved_query(self):
        url = reverse('savedqueries-list')
        data = {
            'user': self.user.id,
            'query_name': 'Test Query',
            'query_description': 'Test Description',
            'first_country': 'Colombia',
            'first_date': '2023-11-22',
            'query_quantity': 1
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

#  for the views

class CommentsViewTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username="testuser")
        self.query = SavedQueries.objects.create(
            user=self.user,
            query_name="Test Query",
            query_description="Test Description",
            first_country="Colombia",
            first_date="2023-11-22",
            query_quantity=1
        )
        self.comment = Comments.objects.create(
            author=self.user,
            text="Test Comment",
            saved_query_reference=self.query
        )

    def test_comments_by_query(self):
        url = reverse('comments-comments_by_query')
        response = self.client.get(url, {'saved_query_id': self.query.id})
        self.assertEqual(response.status_code, 200)

    def test_create_comment(self):
        url = reverse('comments-list')
        data = {
            'author': self.user.id,
            'text': 'Test Comment',
            'saved_query_reference': self.query.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

