import pytest
from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
def test_list_books_api(init_books):
    client = Client()
    response = client.get(reverse('list_books'))

    assert response.status_code == 200
    
    api_data = response.json()
    print(f"{api_data=}")
    
    assert len(api_data)==len(init_books)
    assert api_data==init_books
    