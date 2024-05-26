from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create one post in the test DB
        # for this we need to create a user first
        user = get_user_model().objects.create_user(
            username="testuser", email="testuser@email.com", password="test1234"
        )
        cls.post = Post.objects.create(
            title="Test Title 1", body="This is the test body 1", author=user
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "Test Title 1")
        self.assertEqual(self.post.body, "This is the test body 1")
        self.assertEqual(str(self.post), "Test Title 1")
        self.assertEqual(self.post.get_absolute_url(), "/post/1")

    def test_url_home_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_blog_detail_exists_at_correct_location(self):
        response = self.client.get("/post/1")
        self.assertEqual(response.status_code, 200)

    def test_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "This is the test body 1")

    def test_blog_detail_page(self):
        response = self.client.get(reverse("post_detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 200)
        not_found_response = self.client.get("/post/9999")
        self.assertEqual(not_found_response.status_code, 404)
        self.assertTemplateUsed(response, "blog_detail.html")
        self.assertContains(response, "This is the test body 1")
