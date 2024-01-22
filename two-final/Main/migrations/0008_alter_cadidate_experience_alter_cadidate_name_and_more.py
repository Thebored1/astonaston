# Generated by Django 4.1.7 on 2023-04-24 06:52

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0007_alter_cadidate_options_alter_career_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadidate',
            name='experience',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='cadidate',
            name='name',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(regex=re.compile('^[a-z\\-]+$'))]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(regex=re.compile('^[a-z\\-]+$'))]),
        ),
    ]