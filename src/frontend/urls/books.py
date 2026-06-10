from django.urls import path

import src.frontend.views.books as views

urlpatterns = [
    path('', views.home, name='home'),
    path("filter/category/<int:category_id>", views.book_filter_by_category, name="category_by"),
    path("filter/book/", views.search_books, name="search_by"),
    path('book/', views.book_home, name='book_home'),
    path('book/<int:book_id>', views.book_detail, name='book_detail'),
    path('register', views.register_user, name='register'),
    path('login', views.login_user, name='my_login'),
    path('logout', views.logout_user, name='logout'),
    path('comments/<int:book_id>', views.comments, name='comments_'),
    path("rating/<int:book_id>", views.add_rating, name="add_rating"),
]