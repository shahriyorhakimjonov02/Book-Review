from django.urls import path

import api.views.category as views

urlpatterns = [
    path("list/", views.CategoryListApi.as_view()),
]