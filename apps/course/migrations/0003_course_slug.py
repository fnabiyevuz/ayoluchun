# Generated by Django 4.1.7 on 2023-03-11 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_rename_contentviews_contentview_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(max_length=255, null=True, verbose_name='Slug'),
        ),
    ]