from pyexpat import model
from django.urls import path
from .models import (
    Author, Book, Publisher
)
from .views import (
    home, CustomCreate, CustomDetail, CustomList, PersonFormView,
    PublisherList, PublisherDetail,
)

app_name = 'cviews'

urlpatterns = [
    path('', home, name='home'),
    path('person/', PersonFormView.as_view(), name='person'),

    path('publishers/', CustomList.as_view(model=Publisher), name='publishers'),
    path('publishers/<int:pk>/', CustomDetail.as_view(model=Publisher), name='publisher'),
    path('publisher/create/', CustomCreate.as_view(model=Publisher), name='create-publisher'),
    
    path('authors/', CustomList.as_view(model=Author), name='authors'),
    path('authors/<slug:slug>/', CustomDetail.as_view(model=Author), name='author'),
    path('author/create/', CustomCreate.as_view(model=Author), name='create-author'),
    
    path('books/', CustomList.as_view(model=Book), name='books'),
    path('books/<slug:slug>/', CustomDetail.as_view(model=Book), name='book'),
    path('book/create/', CustomCreate.as_view(model=Book), name='create-book'),
]
