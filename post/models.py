from django.db import models
from django_jalali.db import models as jmodels
import jdatetime


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='posts')
    publish = jmodels.jDateTimeField(default=jdatetime.datetime.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (('d', 'پیش نویس'), ('p', 'منتشر شده'))
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title
