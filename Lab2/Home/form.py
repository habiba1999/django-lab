from django.forms import ModelForm
from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['author_name' , 'title' , 'description','type' , 'rate' , 'views' ]