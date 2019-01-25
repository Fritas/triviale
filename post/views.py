from django.shortcuts import render, get_object_or_404
from .models import Post, Author


# Create your views here.
def post_render(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'post.html', {'post' : post, 'authors': post.authors.all()})


def author_render(request, id):
    author = get_object_or_404(Author, pk=id)
    posts = author.post_set.all()
    return render(request, 'author.html', {'author' : author, 'posts' : posts})

