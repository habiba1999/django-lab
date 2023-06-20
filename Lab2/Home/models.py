# Create your models here.
from django.db import models
from django.utils.text import slugify


class Book(models.Model):
    author_name = models.CharField(max_length=30)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    type= models.CharField(max_length=100)
    rate = models.IntegerField()
    views = models.IntegerField()
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)