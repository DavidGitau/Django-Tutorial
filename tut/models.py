from tkinter import CASCADE
from django.db import models
from django.db.models import Q, F

class CommonInfo(models.Model):
    pK = models.AutoField(primary_key=True)
    first_name = models.CharField('persons first name', max_length=50)
    last_name = models.CharField('persons last name', max_length=50)

    class Meta:
        abstract = True
        ordering = ['first_name']

    def __str__(self):
        name = self.first_name +' '+ self.last_name
        return name


class Person(CommonInfo):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    # pK = models.AutoField(primary_key=True)
    # first_name = models.CharField('person first name', max_length=30)
    # last_name = models.CharField('person last name', max_length=30)
    shirt_size = models.CharField('person shirt size', max_length=1, choices=SHIRT_SIZES, null=True)
    # def __str__(self):
    #     return self.last_name
class MyPerson(Person):
    class Meta:
        proxy = True

    def do_something(self):
        # 
        pass

class Musician(CommonInfo):
    # pK = models.AutoField(primary_key=True)
    # first_name = models.CharField('musician first name', max_length=50)
    # last_name = models.CharField('musician last name', max_length=50)
    instrument = models.CharField('musician instrument', max_length=100)

    # def __str__(self):
    #     return self.first_name +' '+ self.last_name

class Album(CommonInfo):
    # pK = models.AutoField(primary_key=True)
    first_name = None
    last_name = None
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE, verbose_name = 'musician name')
    name = models.CharField('album name', max_length=100)
    release_date = models.DateField('album release date')
    num_stars = models.IntegerField('album stars number')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True, verbose_name = 'name')

    def __str__(self):
        return self.name

# Blog DB 
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline= models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name_plural = 'Entries'

# Q = Author.objects.filter(Q(name__icontains='a')&~Q(name__icontains='i'))
# F = Entry.objects.filter(number_of_comments__lt=F('number_of_pings')*3+100)
