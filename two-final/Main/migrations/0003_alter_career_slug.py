# Generated by Django 4.1.7 on 2023-03-17 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]