from django.urls import path
from api.views import *
from api.serializers import (
    BlogSerializer,
    EntrySerializer
)
from tut.models import (
    Blog,
    Entry
)

appname = 'api'

urlpatterns = [
    path('authors',AuthorList.as_view()),
    path('author/<int:pk>',AuthorDetail.as_view()),
    path(
        'blogs',
        CustomList.as_view(
            queryset = Blog.objects.all(),
            serializer_class = BlogSerializer
        )
    ),
    path(
        'blog/<int:pk>',
        CustomDetail.as_view(
            queryset = Blog.objects.all(),
            serializer_class = BlogSerializer
        )
    ),
    path(
        'entries',
        CustomList.as_view(
            queryset=Entry.objects.all(),
            serializer_class=EntrySerializer
        )
    ),
    path(
        'entry/<int:pk>',
        CustomDetail.as_view(
            queryset=Entry.objects.all(),
            serializer_class=EntrySerializer
        )
    )
]

