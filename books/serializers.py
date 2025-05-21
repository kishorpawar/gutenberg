from rest_framework import serializers
from .models import Book, Author, Subject, Bookshelf, Format, Language

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_year', 'death_year']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']

class BookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookshelf
        fields = ['id', 'name']

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'code']

class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = ['id', 'mime_type', 'url']

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    subjects = SubjectSerializer(many=True)
    bookshelves = BookshelfSerializer(many=True)
    languages = LanguageSerializer(many=True)
    formats = FormatSerializer(many=True)

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'gutenberg_id', 'media_type', 'download_count',
            'authors', 'subjects', 'bookshelves', 'languages', 'formats'
        ]