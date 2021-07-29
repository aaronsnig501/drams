from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from blog.models import Post, Category


class PostTests(APITestCase):
    def test_view_post(self):
        url = reverse("blog:listcreate")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        self.test_category = Category.objects.create(name="django")
        self.test_user = User.objects.create_user(
            username="testuser", password="test", is_superuser=True
        )

        self.client.login(username=self.test_user.username, password="test")

        data = {"title": "New", "author": 1, "excerpt": "new", "content": "new"}
        url = reverse("blog:listcreate")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_update(self):
        client = APIClient()

        self.test_category = Category.objects.create(name="django")
        self.admin_user = User.objects.create_user(
            username="test_admin", password="123456789"
        )
        self.other_user = User.objects.create_user(
            username="test_user", password="123456789"
        )

        test_post = Post.objects.create(
            category_id=1,
            title="Post Title",
            excerpt="Post Excerpt",
            content="Post Content",
            slug="post-title",
            author_id=1,
            status="published",
        )

        client.login(username=self.admin_user, password="123456789")
        url = reverse("blog:detailcreate", kwargs={"pk": 1})

        response = client.put(
            url,
            {
                "id": 1,
                "title": "New",
                "author": 1,
                "excerpt": "New",
                "content": "New",
                "status": "published",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
