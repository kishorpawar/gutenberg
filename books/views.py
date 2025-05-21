from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter

class BookViewSet(mixins.ListModelMixin,
                mixins.RetrieveModelMixin, 
                  viewsets.GenericViewSet):
    queryset = Book.objects.all().prefetch_related(
        'authors', 'subjects', 'bookshelves', 'formats', 'languages'
    ).order_by('-download_count')
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = BookFilter
    ordering_fields = ['download_count', 'title']