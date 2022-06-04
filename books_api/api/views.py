from rest_framework import viewsets, filters

from books.models import BookAuthor, Author, Book
from .serializers import BookAuthorSerializer, AuthorSerializer, BookSerializer


class BookAuthorListViewSet(viewsets.ModelViewSet):
    """Объединить автора и книгу по id"""
    queryset = BookAuthor.objects.all()
    serializer_class = BookAuthorSerializer


class AuthorListViewSet(viewsets.ModelViewSet):
    """Создание, изменение, получение, удаление авторов."""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'books__title',)


class BookListViewSet(viewsets.ModelViewSet):
    """Создание, изменение, получение, удаление книг."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'authors__name',)
