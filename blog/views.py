from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.models import User

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
    post = get_object_or_404(Post, id=id)  # Użycie id zamiast pk
    comments = post.comments.all()
    form = CommentForm()

    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect('post_detail', id=post.id)
        else:
            return redirect('login')

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Jeśli użytkownik nie jest autorem posta, przekieruj go
    if request.user.username != post.author:
        return HttpResponseRedirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('post_detail', args=[post.id]))
    else:
        form = PostForm(instance=post)

    form.fields['title'].widget.attrs.update({'class': 'form-control'})
    form.fields['content'].widget.attrs.update({'class': 'form-control'})

    return render(request, 'blog/edit_post.html', {'form': form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user.username != post.author:
        return HttpResponseForbidden("You don't have permission to do that.")
    
    post.delete()
    return redirect(reverse('home'))


def profile(request, author=None):
    if author:
        profile_user = get_object_or_404(User, username=author)
    else:
        profile_user = request.user

    posts = Post.objects.filter(author=profile_user.username)

    comments = Comment.objects.filter(author=profile_user)


    return render(request, 'blog/profile.html', {
        'profile': profile_user,
        'posts': posts,
        'comments': comments
        })