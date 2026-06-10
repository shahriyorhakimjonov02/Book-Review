from django.urls import path

import src.frontend.views.bookcrud as views

urlpatterns = [
    path('book/list', views.book_list, name='list'),
    path('book/create/', views.create_book, name='create'),
    path('book/update/<int:pk>/', views.book_update, name='update'),
    path('book/delete/<int:pk>/', views.book_delete, name='delete'),
]