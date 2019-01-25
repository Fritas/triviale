from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def post_render(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'post.html', {'post' : post, 'authors': post.authors.all()})



