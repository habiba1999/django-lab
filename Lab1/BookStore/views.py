from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

# Create your views here.

My_Books = [
    {
        "index": 0,
        "id": 1,
        "name": "Sapiens: A Brief History of Humankind",
        "price": 500,
        "description": "This book explores the history of human beings, from the emergence of Homo sapiens in Africa to the present day. It covers a wide range of topics, including the development of language, the rise of agriculture, the creation of religions, and the growth of empires.",
    },
    {
        "index": 1,
        "id": 2,
        "name": "The Power of Now",
        "price": 650,
        "description": "This book is a spiritual guide to living in the present moment. Tolle argues that most human suffering is caused by our attachment to the past or the future, and that we can find peace and happiness by focusing on the present moment. The book provides practical advice and exercises for achieving this state of mindfulness.",
    },
    {
        "index": 2,
        "id": 3,
        "name": "The 7 Habits of Highly Effective People",
        "price": 799,
        "description": "This self-help book is a classic in the genre, and has sold millions of copies worldwide. Covey presents seven habits that he believes are essential for personal and professional success, including taking initiative, setting goals, and communicating effectively.",
    },
    {
        "index": 3,
        "id": 4,
        "name": "The Immortal Life of Henrietta Lacks",
        "price": 1099,
        "description": "This book tells the story of Henrietta Lacks, a woman whose cancer cells were used without her knowledge or consent to develop the first immortal human cell line. Skloot explores the ethical and scientific implications of this case, as well as the impact it had on Lacks' family.",
    },
]


def index(request):
    return render(request, "main/base_layout.html")


def _get_books(book_id):
    for book in My_Books:
        if "id" in book and book["id"] == book_id:
            return book
    return None


def books_list(request):
    my_context = {"books_list": My_Books}
    return render(request, "books/books_list.html", context=my_context)


def book_details(request, **kwargs):
    book_id = kwargs.get("book_id")
    book_object = _get_books(book_id)
    my_context = {
        "book_id": book_object.get("id"),
        "book_name": book_object.get("name"),
        "book_price": book_object.get("price"),
        "book_description": book_object.get("description"),
    }
    return render(request, "books/book_details.html", context=my_context)

def book_delete(request, **kwargs):
    book_id = kwargs.get('book_id')
    book_object = _get_books(book_id)
    if book_object:
        My_Books.remove(book_object)
    return redirect('books:books_list')

def book_update(request, **kwargs):
    book_id = kwargs.get('book_id')
    book_object = _get_books(book_id)
    for book in My_Books:
        if book == book_object:
            book['name'] = f"Update {book_object['name']}"
    return redirect('books:books_list')

def book_add(request):
    new_index = max(book['index'] for book in My_Books) + 1
    new_book = {
        'index': new_index,
        'id': new_index + 1,
        'name':"New Book",
        'price': 750,
        'description': "Book description",
    }
    My_Books.append(new_book)
    return redirect('books:books_list')