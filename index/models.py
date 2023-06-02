from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field
from taggit.managers import TaggableManager


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug  = models.CharField(max_length=250, blank=True)
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)
    def __str__(self):
        return self.title


class Post(models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    book_author = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = CKEditor5Field('Text', config_name='extends')
    status = models.CharField(max_length=10, choices=options, default='published')
    favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)
    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager
    tags = TaggableManager()
    def get_absolute_url(self):
        return reverse("add")
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title