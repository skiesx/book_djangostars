from django.shortcuts import render, redirect, get_object_or_404
from apps.book_app.models import *
from .forms import BookForm

def list_book_page(request):
    context = {}
    context['title'] = "Books"
    if request.GET.get('sort'):
        context['sort'] = request.GET['sort']
        if request.GET['sort'] == "desc":
            context['books'] = Book.objects.all().order_by("-publish_date")
        else:
            context['books'] = Book.objects.all().order_by("publish_date")
    else:
        context['books'] = Book.objects.all()


    return render(request, 'list_book_page.html', context)

def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect("list_book_page")
    else:
        context = {}
        context['title'] = "Add"
        context['form'] = BookForm()
        return render(request, 'edit_book_page.html', context)


def edit_book(request, id_book):
    book = get_object_or_404(Book, id=id_book)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            post = form.save()
            return redirect('list_book_page')
    else:
        context = {}
        context['title'] = "Change"
        context['form'] = BookForm(instance=book)
    return render(request, 'edit_book_page.html', context)

def http_requests_page(request):
        context = {}
        context['http_requests'] = WebRequest.objects.all().order_by("-created")[:10]
        context['title'] = "http_requests"

        return render(request, 'http_requests_page.html', context)
