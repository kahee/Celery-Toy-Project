from __future__ import absolute_import, unicode_literals
from celery import shared_task

from books.models import Book
from books.utils import get_book_detail


@shared_task
def book_detail_save():
    print(f'{book_id} 상세 정보 크롤')

    books = Book.objects.all()

    for book in books:
        get_book_detail(book.book_id)
        print(f'{book.book_id)}가 저장되었습니다.')
    return f'끝'

# @shared_task
# def book_location_save(book_id, location_list):
#     book_location, _ = BookLocation.objects.get_or_create(
#         register_id=location_list[0],
#         location=location_list[1],
#         book_code=location_list[2],
#         book=Book.objects.get(book_id=book_id),
#     )
