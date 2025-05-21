from django_filters import rest_framework as filters
from .models import Book

class BookFilter(filters.FilterSet):
    language = filters.CharFilter(method='filter_language')
    mime_type = filters.CharFilter(method='filter_mime_type')
    topic = filters.CharFilter(method='filter_topic')
    author = filters.CharFilter(field_name='authors__name', lookup_expr='icontains')
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    id = filters.NumberFilter(field_name='gutenberg_id')

    class Meta:
        model = Book
        fields = []

    def filter_language(self, queryset, name, value):
        codes = value.split(',')
        return queryset.filter(languages__code__in=codes)

    def filter_mime_type(self, queryset, name, value):
        mimes = value.split(',')
        return queryset.filter(formats__mime_type__in=mimes)

    def filter_topic(self, queryset, name, value):
        keywords = value.lower().split(',')
        return queryset.filter(
            models.Q(subjects__name__icontains=keywords[0]) |
            models.Q(bookshelves__name__icontains=keywords[0])
        ).distinct()