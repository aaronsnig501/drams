from django.db import models
from django.utils import timezone
from accounts.models import Account


class PostObjects(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="published")


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        ordering = ("-published",)

    options = (("draft", "Draft"), ("published", "Published"))

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date="published")
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="blog_posts"
    )
    status = models.CharField(max_length=10, choices=options, default="published")

    objects = models.Manager()
    post_objects = PostObjects()

    def __str__(self):
        return self.title
