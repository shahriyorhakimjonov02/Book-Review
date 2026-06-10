from django.urls import path

import api.views.user as views

urlpatterns = [
    path('register', views.UserCreateAPIView.as_view()),
    path("me", views.GetMeView.as_view())
]