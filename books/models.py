# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

# Note: Be sure to enable the pg_trgm extension before running migrations:
# CREATE EXTENSION IF NOT EXISTS pg_trgm; 

from django.db import models
from django.contrib.postgres.indexes import GinIndex, BrinIndex


class Author(models.Model):
    birth_year = models.SmallIntegerField(blank=True, null=True)
    death_year = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'books_author'
        indexes = [
            GinIndex(fields=['name'], name='author_name_trgm', opclasses=['gin_trgm_ops']),
        ]

    def __str__(self):
        return self.name


class Bookshelf(models.Model):
    name = models.CharField(unique=True, max_length=64)

    class Meta:
        db_table = 'books_bookshelf'
        indexes = [
            GinIndex(fields=['name'], name='bookshelf_name_trgm', opclasses=['gin_trgm_ops']),
        ]

    def __str__(self):
        return self.name


class Language(models.Model):
    code = models.CharField(unique=True, max_length=4)

    class Meta:
        db_table = 'books_language'
        indexes = [
            models.Index(fields=['code'], name='language_code_idx'),
        ]

    def __str__(self):
        return self.code


class Subject(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        db_table = 'books_subject'
        indexes = [
            GinIndex(fields=['name'], name='subject_name_trgm', opclasses=['gin_trgm_ops']),
        ]

    def __str__(self):
        return self.name


class Book(models.Model):
    download_count = models.IntegerField(blank=True, null=True)
    gutenberg_id = models.IntegerField(unique=True)
    media_type = models.CharField(max_length=16)
    title = models.CharField(max_length=1024, blank=True, null=True)

    authors = models.ManyToManyField(
        Author,
        related_name='books',
        db_table='books_book_authors'
    )
    bookshelves = models.ManyToManyField(
        Bookshelf,
        related_name='books',
        db_table='books_book_bookshelves'
    )
    languages = models.ManyToManyField(
        Language,
        related_name='books',
        db_table='books_book_languages'
    )
    subjects = models.ManyToManyField(
        Subject,
        related_name='books',
        db_table='books_book_subjects'
    )

    class Meta:
        db_table = 'books_book'
        indexes = [
            models.Index(fields=['download_count'], name='book_download_idx'),
            GinIndex(fields=['title'], name='book_title_trgm', opclasses=['gin_trgm_ops']),
            models.Index(fields=['gutenberg_id'], name='book_gutenberg_id_idx'),
        ]

    def __str__(self):
        return self.title or f"Book {self.gutenberg_id}"


class Format(models.Model):
    mime_type = models.CharField(max_length=32)
    url = models.CharField(max_length=256)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='formats')

    class Meta:
        db_table = 'books_format'
        indexes = [
            models.Index(fields=['mime_type'], name='format_mime_idx'),
        ]

    def __str__(self):
        return f"{self.mime_type} ({self.book.title})"
