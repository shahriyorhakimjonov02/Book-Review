from django.urls import path

import src.frontend.views.categorycrud as views

urlpatterns = [
    path('category/list', views.category_list, name='list-category'),
    path('category/create/', views.category_create, name='category-create'),
    path('category/update/<int:pk>/', views.category_update, name='category-update'),
    path('category/delete/<int:pk>/', views.category_delete, name='category-delete'),
]