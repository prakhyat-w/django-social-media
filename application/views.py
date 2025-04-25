from django.shortcuts import render
from .models import Post
from .forms import Postform, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

def all_posts(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'all_posts.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = Postform(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('all_posts')
    else:
        form = Postform()
    return render(request, 'create_post.html',{'form': form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id, user = request.user)
    if request.method == 'POST':
        form = Postform(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('all_posts')
    else:
        form = Postform(instance=post)
    return render(request, 'create_post.html',{'form': form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id, user = request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('all_posts')
    return render(request, 'confirm_delete.html', {'post':post})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('all_posts')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def about(request):
    return render(request, 'about.html')