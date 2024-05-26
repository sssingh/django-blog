import uuid
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(
        max_length=200, null=True, blank=True, default="default_blog_image.jpg"
    )
    image_credit = models.CharField(
        max_length=200, null=True, blank=True, default="Unknown user"
    )
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now=True, editable=False)
    id = models.CharField(
        max_length=300, default=uuid.uuid4, primary_key=True, editable=False
    )
    # id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail-post", kwargs={"pk": self.pk})
