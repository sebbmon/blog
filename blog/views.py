from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import PostForm

def home(request):
    posts = Post.objects.all()  # Pobieranie wszystkich postów
    return render(request, 'blog/home.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)  # Pobieranie posta na podstawie ID
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Tworzymy nowy post bez zapisywania go jeszcze do bazy
            post = form.save(commit=False)
            # Ustawiamy autora na aktualnie zalogowanego użytkownika
            post.author = request.user
            # Ustawiamy daty
            post.created_at = post.updated_at = timezone.now()
            post.published_at = timezone.now()  # Możesz ustawić inną logikę, np. opóźnienie
            post.save()
            return redirect('profile')  # Po zapisaniu, przekierowanie na stronę profilu
    else:
        form = PostForm()

    return render(request, 'blog/new_post.html', {'form': form})

def post_list(request):
    posts = Post.objects.all()  # Pobranie wszystkich postów
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)  # Pobranie posta na podstawie ID
    return render(request, 'blog/post_detail.html', {'post': post})

