from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm


# Create your views here.


def index(request):
    title = 'Статьи'
    posts = Post.objects.all()
    context = {'title': title, 'posts': posts}
    return render(request,'index.html', context)

def register(request):
    title = 'Регистрация нового пользователя'

    return render(request,'register.html', {'title': title})

def login(request):
    title = 'Ввод логина и пароля'
    return render(request,'login.html', {'title': title})

def add_post(request):
    title = 'Добавить статью'
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Перенаправляем обратно на главную страницу
    else:
        form = PostForm()

    posts = Post.objects.all()
    context = {'title': title,'articles': posts, 'form': form}
    return render(request, 'add_post.html', context)


def edit_post(request, id):
    title = 'Редактирование поста'
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')  #
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form, 'post': post})

def delete_post(request, id):
    title = 'Подтверждение удаления'
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, 'delete_confirmation.html', {'post': post})


