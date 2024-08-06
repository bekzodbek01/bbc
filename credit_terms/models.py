from django.db import models


class Credit_terms(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='Credit_terms/file/', blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Credit_terms'
        verbose_name_plural = 'Credit_terms'

    def __str__(self):
        return self.title







