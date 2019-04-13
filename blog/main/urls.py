from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('get-all-posts',views.BlogAPI.as_view()),
    path('get-post/<int:pk>',views.SingleBlogAPI.as_view()),
    path('send-comment',views.CreateCommentAPI.as_view()),
]
