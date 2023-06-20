from django.urls import path
from .views import index, books_list,book_details,book_delete,book_update,book_add

app_name = 'books'

urlpatterns = [
    path('', index, name='bookStore-index'),
    path('books_list/', books_list, name="books_list"),
    path('book_details/<int:book_id>', book_details, name="book_details"),
    path('book_delete/<int:task_id>', book_delete, name="book_delete"),
    path('book_update/<int:task_id>', book_update, name="book_update"),
    path('book_add/', book_add, name="book_add")
   
]
