import pytest
from app01.models import Book


@pytest.fixture
def init_books():
    b1: Book = Book.objects.create(name="Python")
    b2: Book = Book.objects.create(name="Java")

    return [
        {"id": b1.pk, "name": b1.name},
        {"id": b2.pk, "name": b2.name}
    ]