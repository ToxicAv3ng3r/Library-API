from rest_framework import serializers, validators

from books.models import BookAuthor, Author, Book


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = Book
        fields = (
            'id',
            'authors',
            'title',
            'description',
            'pub_date',
        )
        read_only_fields = ('pub_date',)


class BookAuthorSerializer(serializers.ModelSerializer):
    validators = [
        validators.UniqueTogetherValidator(
            BookAuthor.objects.all(),
            fields=('author', 'book',),
            message='Такая запись уже есть!'
        )
    ]

    class Meta:
        fields = (
            'id',
            'author',
            'book'
        )
        model = BookAuthor


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = Author
        fields = (
            'id',
            'name',
            'pub_date',
            'books',
        )
        read_only_fields = (
            'pub_date',
            'books',
        )
