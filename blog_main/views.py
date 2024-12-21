from django.shortcuts import render
from blog.models import Post
from django.core.paginator import Paginator

def home(request):
    #posts = Post.objects.all()
    posts = Post.objects.order_by('-created_at')
    paginator = Paginator(posts, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts' : posts,
        'page_obj': page_obj,
    }

    return render(request, 'home.html', context)

def new_post(request):
    if request.method == 'POST':
        pass
    return render(request, 'new_post.html')