from django.shortcuts import render, redirect
from django.http import HttpResponse
from src.core.forms import BookForm
from src.core.models import Book


def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = BookForm()
    return render(request, "create.html", {"form": form})

#list view
def book_list(request):
    books = Book.objects.all()
    return render(request, "list.html", {"books": books})

def book_update(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('list')

    else:
        form = BookForm(instance=book)
    return render(request, "update.html", {'form': form})

def book_delete(request, pk):
    book = Book.objects.get(id= pk)
    if request.method == 'POST':
        book.delete()
    return redirect('list')
