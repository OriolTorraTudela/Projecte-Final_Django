from django.db import models
from django.urls import reverse
from django.utils.text import slugify 


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name  = models.CharField(max_length=30)
    email      = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

class Tag(models.Model):
    tag = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag-posts', args=[self.tag])

class Post(models.Model):
    title      = models.CharField(max_length=100)
    excerpt    = models.TextField()
    image_name = models.CharField(max_length=100)
    date       = models.DateField()
    slug       = models.SlugField(default="", blank=True, null=False, db_index=True)
    content    = models.TextField()
    author     = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    tags       = models.ManyToManyField(Tag, related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts-detail-page', args=[self.slug])

