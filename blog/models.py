from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
class publishedArticlemanager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='publish')


class Article(models.Model):
        STATUS = (
            ('draft', 'Draft'),
            ('publish', 'Publish')
        )
        title = models.CharField(max_length=120)
        slug = models.SlugField(max_length=120, unique=True)
        writer = models.ForeignKey(User, on_delete=models.CASCADE)
        body =RichTextUploadingField()
        publish = models.DateTimeField(default=timezone.now)
        updated = models.DateTimeField(auto_now=True)
        status = models.CharField(max_length=20, choices=STATUS, default='draft')
        objects = models.Manager()
        published = publishedArticlemanager()
        objects=models.Manager()

        def get_absolute_url(self):
            return reverse('blog:article_detail', args=[self.id, self.slug])

        def __str__(self):
            return self.title







