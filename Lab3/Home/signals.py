from django.db.models.signals import pre_save 
from django.dispatch import receiver
from .models import Book , Isbn

@receiver(pre_save , sender=Book)
def create_and_assign_isbn_to(instance ,**kwargs):
    if instance.isbn:
        return;

    isbn = Isbn.objects.create(
    author_title='Doctor Kim',
    book_title='My Book Title'
    )
    instance.isbn = isbn



