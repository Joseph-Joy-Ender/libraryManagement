import uuid

from django.db import models
from django.conf import settings


# Create your models here.


class Book(models.Model):
    BOOK_CHOICES = [
        ('P', 'Politics'),
        ('F', 'Finance'),
        ('R', 'Romance'),
        ('T', 'Technology')
    ]
    title = models.CharField(max_length=255)
    summary = models.TextField
    ISBN = models.CharField(max_length=20)
    genre = models.CharField(max_length=1, choices=BOOK_CHOICES, default='F')
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.ISBN}"


class Author(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.date_of_birth}"


class Language(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


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
