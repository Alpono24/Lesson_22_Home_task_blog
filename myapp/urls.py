from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import index, add_post, edit_post, delete_post, post_detail


from .views import register_view

urlpatterns = [
    path('', index, name='index'),

    path('post/<int:id>/', post_detail, name='post_detail'),


    path('add_post/', add_post, name='add_post'),
    path('edit/<int:id>/', edit_post, name='edit_post'),
    path('delete/<int:id>/', delete_post, name='delete_post'),

    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]