from django.db import models
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator 


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True, blank=True)
    photo = models.ImageField()
    body = RichTextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Career(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    experience = models.IntegerField(blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    description = RichTextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Career, self).save(*args, **kwargs)

    def __str__(self):
            return self.title
    
from django.core.validators import RegexValidator

#AlphanumericValidator = RegexValidator(r'^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
import re
namespace_regex = re.compile(r'^[a-z\- \t\a-z]+$')

class cadidate(models.Model):
    name = models.CharField(max_length=255, validators=[RegexValidator(regex=namespace_regex)] )
    email = models.EmailField()
    phone_no = PhoneNumberField()
    experience = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)])
    resume = models.FileField(upload_to='resume')
    job = models.CharField(max_length=255, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.name or ''
    
class Contact(models.Model):
    name = models.CharField(max_length=255, validators=[RegexValidator(regex=namespace_regex)] )
    email = models.EmailField()
    phone_no = PhoneNumberField()
    company_name = models.CharField(max_length=255)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.name or ''
            
