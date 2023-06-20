from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from Home.models import Book
from .form import BookForm


def index(request):
    books = Book.objects.all().values()
    return render(request, "home/index.html", {"books": books})


def show(request, id):
    book = Book.objects.get(pk=id)
    return render(request, "home/show.html", {"book": book})


def edit(request, id):

    book = Book.objects.get(pk=id)
    form = BookForm(instance=book)
    return render(request, "home/edit.html", {'form':form , 'book':book})


def create(request):

    form = BookForm()
    return render(request, "home/create.html" , {"form" : form})


def store(request):

    form = BookForm(request.POST)
    if form.is_valid:
       form.save()
    return redirect('BookStore:book-index')

@csrf_protect
def update(request, id):
    book = Book.objects.get(pk=id)
    form = BookForm(request.POST, instance=book)
    if form.is_valid():  # Call is_valid() as a function
        form.save()
        return redirect("BookStore:book-index")
    else:
        # Handle invalid form data
        # You can display the form errors or perform any necessary actions
        pass



def destroy(request, id):

    book = Book.objects.get(pk=id)
    book.delete()
    return redirect("BookStore:book-index")