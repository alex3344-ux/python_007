# Generated by Django 4.1.5 on 2023-02-22 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
    ]
