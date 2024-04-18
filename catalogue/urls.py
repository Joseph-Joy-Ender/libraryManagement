from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.add_book, name='add_book'),
    path('books/<int:pk>/', views.book_details, name='book_details'),
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:pk>/', views.author_details, name='author_details')

]