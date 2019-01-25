from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def post_render(request, id):
    print("\n\n\n\n %d \n\n\n\n\n" %(id))
    post = get_object_or_404(Post, pk=id)
    print("\n\n\n\n", post.authors, "\n\n\n\n")
    return render(request, 'post.html', {'post' : post})



