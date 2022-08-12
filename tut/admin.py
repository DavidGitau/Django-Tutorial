from django.contrib import admin
from .models import (
    Person,
    Musician,
    Album,
    Fruit,
    Entry,
    Author,
    Blog
)

admin.site.register(Person)
admin.site.register(Fruit)
admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Entry)
admin.site.register(Author)
admin.site.register(Blog)