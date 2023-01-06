from rest_framework.serializers import ModelSerializer
from tut.models import (
    Author,
    Blog,
    Entry
)


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class EntrySerializer(ModelSerializer):
    blog = BlogSerializer()
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Entry
        fields = '__all__'
