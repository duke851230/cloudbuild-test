from django.contrib import admin
from django.urls import path

from app01.views import list_books

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', list_books, name="list_books")
]
