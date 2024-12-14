from django.shortcuts import render
from blog.models import Post

def home(request):
    posts = Post.objects.all()

    context = {
        'posts' : posts,
    }

    return render(request, 'home.html', context)

def new_post(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'new_post.html')