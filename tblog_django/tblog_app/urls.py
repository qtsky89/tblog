from django.contrib import admin
from django.urls import path, include
from tblog_app import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]
