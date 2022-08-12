from ntpath import join
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import lazy as l
import uuid


class Common(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        u = uuid.uuid4()
        self.slug = '-'.join((slugify(self.name), slugify(u)))
        super().save(*args, **kwargs)


class Publisher(Common):
    # name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    last_accessed = models.DateTimeField()

    class Meta:
        ordering = ['-name']

    # def __str__(self):
    #     return self.name


class Author(Common):
    salutation = models.CharField(max_length=10)
    # name = models.CharField(max_length=200)
    email = models.EmailField()
    # slug = models.SlugField(unique=True, blank=True)
    # headshot = models.ImageField(upload_to='images/author_headshots')

    # def save(self, *args, **kwargs):
    #     u = uuid.uuid4()
    #     self.slug = '-'.join((slugify(self.name), slugify(u)))
    #     super(Author, self).save(*args, **kwargs)

    # def __str__(self):
    #     return self.name

    def get_absolute_url(self):
        return reverse("tut:cviews:author", kwargs={"slug": self.slug})


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    publication_date = models.DateField()

    def get_absolute_url(self):
        return reverse("tut:cviews:books", kwargs={"pk": self.pk})
