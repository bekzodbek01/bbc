
from django.db import models

# Create your models here.


class News(models):
    title = models.CharField(max_length=60)
    image = models.FileField(upload_to='image', blank=True, null=True)
    video = models.FileField(upload_to='video', blank=True, null=True)
    link = models.URLField(verbose_name='link', blank=True, null=True)
    context = models.TextField(blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)