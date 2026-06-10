from django.shortcuts import render, redirect, get_object_or_404
from unicodedata import category
from django.db.models import Avg
from src.core.forms import CreateUserForm , LoginForm
import src.core.models as models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


def home(request,):
    object_list = models.Book.objects.all().order_by("-id")[:6]
    category_list = models.Category.objects.all()

    for book in object_list:
        book.avg_rating = models.Rating.objects.filter(book=book).aggregate(
            Avg("rating")
        )["rating__avg"]


    context = {
        "object_list": object_list,
        "category_list": category_list,
    }
    return render(request, "home.html", context)

def book_filter_by_category(request, category_id):
    object_list = models.Book.objects.filter(category_id=category_id)
    category_list = models.Category.objects.all()
    context = {
        "object_list": object_list,
        "category_list": category_list,
    }
    return render(request, "home.html", context)

def search_books(request):
    query = request.GET.get("search")

    object_list = models.Book.objects.all()

    if query:
        object_list = object_list.filter(name__icontains=query)

    return render(request, "home.html", {
        "object_list": object_list,
        "category_list": models.Category.objects.all()
    })

def book_home(request):
    object_list = models.Book.objects.all().order_by("-id")
    category_list = models.Category.objects.all()

    for book in object_list:
        book.avg_rating = models.Rating.objects.filter(book=book).aggregate(
            Avg("rating")
        )["rating__avg"]

    context = {
        "object_list": object_list,
        "category_list": category_list,
    }
    return render(request, "home.html", context)


def book_detail(request, book_id):
    category_list = models.Category.objects.all()
    book = models.Book.objects.get(id=book_id)

    avg_rating = models.Rating.objects.filter(book=book).aggregate(
        Avg("rating")
    )["rating__avg"]

    return render(request, "details.html", {
        "book": book,
        "category_list": category_list,
        "avg_rating": avg_rating,
    })

def register_user(request):

    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()
            return redirect("my_login")

    context = {"form": form}

    return render(request, "register.html", context)

def login_user(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:

                auth.login(request, user)
                return redirect("home")

    context = {"form": form}

    return render(request, "login.html", context)

def logout_user(request):
    auth.logout(request)
    return redirect("home")

@login_required(login_url="login")
def comments(request, book_id):
     user = request.user
     comment = request.POST.get("comment")
     book = get_object_or_404(models.Book, pk=book_id)
     models.Comment.objects.create(user=user, book=book, comment=comment)

     return redirect("book_detail", book_id=book_id,)

@login_required(login_url="login")
def add_rating(request, book_id):

    book = get_object_or_404(models.Book, pk=book_id)

    rating_value = request.POST.get("rating")

    models.Rating.objects.update_or_create(
        user=request.user,
        book=book,
        defaults={
            "rating": rating_value
        }
    )

    return redirect("book_detail", book_id=book_id)



