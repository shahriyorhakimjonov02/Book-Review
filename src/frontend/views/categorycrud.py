from django.shortcuts import render, redirect
from django.http import HttpResponse
from src.core.forms import CategoryForm
from src.core.models import Category

def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list-category")
    else:
        form = CategoryForm()

    return render(request, "create.html", {"form":form})

def category_list(request):
    category = Category.objects.all()
    return render(request, "list-category.html", {"category":category})

def category_update(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():
            form.save()
            return redirect('list-category')

    else:
        form = CategoryForm(instance=category)
    return render(request, "update.html", {'form': form})

def category_delete(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        category.delete()
    return redirect('list-category')