from django.conf import settings
from django.db import models
from django.utils import timezone


class News(models.Model):
    published_date = models.DateTimeField(default=timezone.now())
    title = models.CharField(max_length=300)
    text = models.TextField()
    author = models.CharField(max_length=100)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
