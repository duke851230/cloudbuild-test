from django.http.response import JsonResponse
from app01.models import Book


def list_books(request):
    books = Book.objects.all().values('id', 'name')

    return JsonResponse(
        data=list(books),
        safe=False
    )