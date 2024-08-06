from django.db import models


class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.FileField(upload_to='About/image/', blank=True, null=True)
    order = models.IntegerField(default=0)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=255)
    phone = models.CharField(max_length=17)
    description = models.TextField()
    image = models.FileField(upload_to='News/image/', blank=True, null=True)
    order = models.IntegerField(default=0)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title


class Connection(models.Model):
    title = models.CharField(max_length=60)
    longitude = models.FloatField()
    latitude = models.FloatField()
    order = models.IntegerField(default=0)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Connection'
        verbose_name_plural = 'Connection'

    def __str__(self):
        return self.title


class Contact(models.Model):
    phone = models.CharField(max_length=17)
    email = models.EmailField()
    telegram = models.URLField(verbose_name='link', blank=True, null=True)
    instagram = models.URLField(verbose_name='link', blank=True, null=True)
    facebook = models.URLField(verbose_name='link', blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'









