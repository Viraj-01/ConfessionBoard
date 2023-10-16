# confessions/urls.py

from django.urls import path
from .views import (
    confession_list,
    submit_confession,
    add_comment,
    like_dislike_confession,
    like_dislike_comment,
)

urlpatterns = [
    path('confessions/', confession_list, name='confession_list'),
    path('submit_confession/', submit_confession, name='submit_confession'),
    path('add_comment/<int:confession_id>/', add_comment, name='add_comment'),
    path('like_dislike_confession/<int:confession_id>/<str:action>/', like_dislike_confession, name='like_dislike_confession'),
    path('like_dislike_comment/<int:comment_id>/<str:action>/', like_dislike_comment, name='like_dislike_comment'),
    # Add other URL patterns as needed
]
