from django.urls import path
from .views import post_render, author_render

urlpatterns = [
    path('<int:id>/', post_render, name='post'),
    path('author/<int:id>', author_render, name='author')
]