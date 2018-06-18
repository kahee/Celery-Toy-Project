from celery import shared_task

from books.models import Book, BookLocation
from config.celery import app


@app.task(bind=True)
def book_detail_save(self, book_id, book_info_dict):
    print(f'{book_id} 상세 정보 크롤')
    book_info, _ = Book.objects.get_or_create(
        book_id=book_id,
        book_type=book_info_dict.get('자료유형', ' '),
        book_author=book_info_dict.get('서명 / 저자', ' '),
        book_personnel_author=book_info_dict.get('개인저자', ' '),
        book_issue=book_info_dict.get('발행사항', ' '),
        book_form=book_info_dict.get('형태사항', ' '),
        ISBN=book_info_dict.get('ISBN', ' '),
    )


@shared_task
def book_location_save(book_id, location_list):
    book_location, _ = BookLocation.objects.get_or_create(
        register_id=location_list[0],
        location=location_list[1],
        book_code=location_list[2],
        book=Book.objects.get(book_id=book_id),
    )
