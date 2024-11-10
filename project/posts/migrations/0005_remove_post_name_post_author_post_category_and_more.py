# Generated by Django 5.1.3 on 2024-11-10 06:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('categories', '0002_rename_categories_category'),
        ('posts', '0004_alter_post_content_alter_post_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='name',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='author.author'),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(default=None, to='categories.category'),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(default=None, max_length=500),
        ),
    ]
