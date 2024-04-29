import uuid

from django.db import models
from django.conf import settings

from catalogue.validators import validate_file_size


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    ISBN = models.CharField(max_length=13)
    genre = models.ManyToManyField(Genre)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.ISBN}"

    def list_genre(self):
        return ','.join(genre.name for genre in self.genre.all()[:2])


class BookImage(models.Model):
    book_image = models.ImageField(upload_to='catalogue/images', validators=[validate_file_size])
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_image')

    # def __str__(self):
    #     return f"{self.book_image}"


class Author(models.Model):
    name = models.CharField(max_length=20)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.date_of_birth}"


class Language(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Review(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.message}"


class BookInstance(models.Model):
    AVAILABLE = 'A',
    NOT_AVAILABLE = 'N',
    LOAN_STATUS = [
        ('A', "AVAILABLE"),
        ('N', "NOT_AVAILABLE")
    ]
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    due_date = models.DateField()
    status = models.CharField(max_length=1, choices=LOAN_STATUS, default='A')
    borrower = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='borrower')
    book = models.ForeignKey(Book, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.due_date} {self.status}"
