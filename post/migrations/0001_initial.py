# Generated by Django 3.2.2 on 2021-05-10 08:29

from django.db import migrations, models
import django_jalali.db.models
import jdatetime


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(allow_unicode=True, max_length=100, unique=True)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='posts')),
                ('publish', django_jalali.db.models.jDateTimeField(default=jdatetime.datetime.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('d', 'پیش نویس'), ('p', 'منتشر شده')], max_length=1)),
            ],
        ),
    ]
