from django.conf import settings
from django.db import models
from django.utils import timezone
from .translit import prepare_url


class News(models.Model):
    published_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=300)
    text = models.TextField()
    author = models.CharField(max_length=100)
    tr = models.TextField(editable=True, default="")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.tr = self.get_translit_name()
        super().save(*args, **kwargs)

    def get_translit_name(self):
        return prepare_url(self.title)
