from django.urls import path, include
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()

router.register('books', views.BookViewSet, 'books')
router.register('author', views.AuthorViewSet, 'authors')

review_router = routers.NestedDefaultRouter(router, 'books', lookup='book')
review_router.register('review', views.ReviewViewSet, 'review')

urlpatterns = [
    path("", include(router.urls)),
    path("", include(review_router.urls)),
    path("authors/", views.AuthorGenericList.as_view(), name="author"),
    path("authors/<int:pk>", views.AuthorGenericDetail.as_view(), name="author_detail")
]
# urlpatterns = [
#     path('books/', views.add_book, name='add_book'),
#     path('books/<int:pk>/', views.book_details, name='book_details'),
#     path('authors/', views.author_list, name='author_list'),
#     path('authors/<int:pk>/', views.author_details, name='author_details')
#
# ]
