from django.urls import path, include

urlpatterns = [
    path('category/', include('api.urls.category')),
    path('book/', include('api.urls.book')),
    path('user/', include('api.urls.user')),
]