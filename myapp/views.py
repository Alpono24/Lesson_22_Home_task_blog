from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm


from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    title = 'Статьи'
    posts = Post.objects.all()
    context = {'title': title, 'posts': posts}
    return render(request,'index.html', context)


#
# def post_detail(request, pk):
#     post = get_object_or_404(request, pk=pk)
#     return render(request, 'post_detail.html', {'post': post})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post_detail.html', {'post': post})


# @login_required(login_url='/login/')
# def add_post(request):
#     title = 'Добавить статью'
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = PostForm()
#
#     posts = Post.objects.all()
#     context = {'title': title,'articles': posts, 'form': form}
#     return render(request, 'add_post.html', context)


@login_required(login_url='/login/')
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # устанавливаем текущего пользователя как автора
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})


@login_required(login_url='/login/')
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

# @login_required(login_url='/login/')
# def edit_post(request, id):
#     title = 'Редактирование поста'
#     post = get_object_or_404(Post, id=id)
#     if request.method == 'POST':
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user  # устанавливаем текущего пользователя как автора
#             post.save()
#             return redirect('index')  #
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'edit_post.html', {'form': form, 'post': post})


@login_required(login_url='/login/')
def delete_post(request, id):
    title = 'Подтверждение удаления'
    post = get_object_or_404(Post, id=id)

    if post.author != request.user:
        return render(request, 'action_prohibited.html')
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, 'delete_confirmation.html', {'post': post})



#Представление для регистрации в блоге

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # хэшируем пароль
            user.save()
            login(request, user)  # сразу авторизуем пользователя
            return redirect('products')  # редирект на список товаров
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})