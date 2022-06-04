# Generated by Django 2.2.16 on 2022-06-04 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя автора')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления автора в библиотеку')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название книги')),
                ('description', models.TextField(verbose_name='Описание книги')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления книги в библиотеку')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(through='books.BookAuthor', to='books.Author'),
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(through='books.BookAuthor', to='books.Book'),
        ),
    ]
