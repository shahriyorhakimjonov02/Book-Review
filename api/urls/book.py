from django.urls import path

import api.views.book as views

urlpatterns = [
    path("comments/write", views.WriteCommentAPIView.as_view()),
    path("list/", views.BookListAPIView.as_view()),
    path("comments/list", views.CommentListAPIView.as_view()),
    path("detail/<int:pk>", views.BookDetailAPIView.as_view()),
    path("rating", views.AddRatingAPIView.as_view()),
    # path("rating/list", views.RatingListAPIView.as_view()),
]