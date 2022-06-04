from django.contrib import admin

from .models import Author, Book, BookAuthor


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'pub_date',
    )
    search_fields = (
        'name',
    )
    list_editable = (
        'name',
    )
    list_filter = (
        'pub_date',
    )
    empty_value_display = '-пусто-'


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'description',
        'pub_date',
    )
    search_fields = (
        'title',
    )
    list_editable = (
        'title',
        'description',
    )


class BookAuthorAdmin(admin.ModelAdmin):
    list_display = (
        'book',
        'author',
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookAuthor, BookAuthorAdmin)
