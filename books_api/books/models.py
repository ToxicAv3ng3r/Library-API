from django.db import models


class Author(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя автора'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления автора в библиотеку'
    )
    books = models.ManyToManyField(
        'Book',
        through='BookAuthor'
    )

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название книги'
    )
    description = models.TextField(
        verbose_name='Описание книги'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления книги в библиотеку'
    )
    authors = models.ManyToManyField(
        Author,
        through='BookAuthor'
    )

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title


class BookAuthor(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Книги по автору'
        verbose_name_plural = 'Книги по авторам'

    def __str__(self):
        return f'{self.author.name}: {self.book.title}'
