from django_filters import rest_framework as filters
from tut.models import Author


class AuthorFilter(filters.FilterSet):
    class Meta:
        model = Author 
        fields = {
            'id': ['exact', 'lt', 'gt'],
            'name': ['exact', 'icontains']
        }