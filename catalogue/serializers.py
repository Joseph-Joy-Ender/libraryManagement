from rest_framework import serializers
from catalogue.models import Book
from catalogue.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'date_of_birth']


class BookSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        queryset=Author.objects.all(),
        view_name='author_details'
    )

    class Meta:
        model = Book
        fields = ['title', 'summary', 'ISBN', 'author']
