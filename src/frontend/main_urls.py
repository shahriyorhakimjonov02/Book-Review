from django.urls import include, path

urlpatterns = [
    path('', include('src.frontend.urls.books')),
    path('', include('src.frontend.urls.book-crud')),
    path('', include('src.frontend.urls.category-crud')),
]