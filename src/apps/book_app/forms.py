from django import forms

from .models import Book

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'author', 'isbn', 'price', 'publish_date',)
        widgets = {
            'publish_date' : forms.DateInput(attrs={'type':'date', 'data-date-format':'DD MMMM YYYY'})
        }
