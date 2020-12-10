from django.db import models
from .translit import prepare_url
from gdstorage.storage import GoogleDriveStorage

class News(models.Model):
    published_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=300)
    text = models.TextField()
    author = models.CharField(max_length=100)
    tr = models.TextField(editable=False, default="")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.tr = self.get_translit_name()
        super().save(*args, **kwargs)

    def get_translit_name(self):
        return prepare_url(self.title)


class Feedback(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    telephoneNumber = models.PositiveBigIntegerField()
    message = models.TextField(max_length=1000)
    file = models.FileField(upload_to='djFiles', storage=GoogleDriveStorage())

    def __str__(self):
        return self.surname