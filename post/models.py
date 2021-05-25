from django.db import models
from django_jalali.db import models as jmodels
import jdatetime
from extensions.utils import change_format_date


# New Managers
class PostManager(models.Manager):
    def published(self):
        return self.filter(status='p')

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True, verbose_name='آدرس بندی')
    status = models.BooleanField(default=True, verbose_name='آیا نمایش داده شود؟')
    position = models.IntegerField(verbose_name='پوزیشن')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ('position',)


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True, verbose_name='آدرس مقاله')
    category = models.ManyToManyField(to=Category,verbose_name='دسته بندی',related_name="posts")
    description = models.TextField(verbose_name='محتوا')
    thumbnail = models.ImageField(upload_to='posts', verbose_name='تصویر مقاله')
    publish = jmodels.jDateTimeField(default=jdatetime.datetime.now, verbose_name='تاریخ انتشار')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (('d', 'پیش نویس'), ('p', 'منتشر شده'))
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')

    def __str__(self):
        return self.title

    def jpublish(self):
        return change_format_date(self.publish)

    def category_published(self):
        return self.category.filter(status=True)
    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست ها"
        ordering = ('-publish',)

    jpublish.short_description = "زمان انتشار"

    objects = PostManager()