from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from catalogue.models import Book, Author, Review, BookImage
from catalogue.pagination import DefaultPagination
from catalogue.permissions import IsAdminOrReadOnly
from catalogue.serializers import BookSerializer, AuthorSerializer, ReviewSerializer, BookImageSerializer


# Create your views here.

class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author']

    def get_serializer_context(self):
        return {'request': self.request}


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']

    def get_serializer_context(self):
        return {'request': self.request}


class BookImageViewSet(ModelViewSet):
    queryset = BookImage.objects.all()
    serializer_class = BookImageSerializer


class ReviewViewSet(ModelViewSet):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(book_id=self.kwargs['book_pk'])

    def get_serializer_context(self):
        return {'book_pk': self.kwargs['book_pk']}


# GenericApiView
class BookGenericList(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class BookGenericDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorGenericList(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorGenericDetail(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ReviewGenericList(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = AuthorSerializer

# @api_view(['GET', 'POST'])
# def add_book(request):
#     if request.method == 'GET':
#         book = Book.objects.all()
#         serializer = BookSerializer(book, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = BookSerializer(Book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def book_details(request, pk):
#     book = get_object_or_404(Book, id=pk)
#     if request.method == 'GET':
#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = BookSerializer(book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# def author_list(request):
#     if request.method == 'GET':
#         author = Author.objects.all()
#         serializer = AuthorSerializer(author, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = AuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def author_details(request, pk):
#     author = get_object_or_404(Author, id=pk)
#     if request.method == 'GET':
#         serializer = AuthorSerializer(author)
#         author_qrcode = segno.make_qr('Welcome to Lagos')
#         author_qrcode.save('qrcode.png')
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = BookSerializer(author, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
