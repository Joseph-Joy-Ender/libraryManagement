from rest_framework import serializers
from catalogue.models import Book, Review
from catalogue.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'date_of_birth']


class BookSerializer(serializers.ModelSerializer):
    # author = serializers.HyperlinkedRelatedField(
    #     queryset=Author.objects.all(),
    #     view_name='author_details'
    # )

    class Meta:
        model = Book
        fields = ['title', 'summary', 'ISBN', 'author']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'message']

    def create(self, validated_data):
        book_pk = self.context['book_pk']

        return Review.objects.create(book_id=book_pk,**validated_data)