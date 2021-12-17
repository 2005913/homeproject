from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostFrom
from django.urls import reverse_lazy
from django.views.generic import *

def post_edit(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method=="POST":
        form = PostFrom(request.POST, instance=post)
        if form.is_valid():
            post= form.save(commit=False)
            post.author=request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail',pk=post.pk)
    else:
        form= PostFrom(instance=post)
    return render(request,'blog/post_edit.html',{'form':form})


def post_new(request):
    if request.method== 'POST':
        form = PostFrom(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form=PostFrom()

    return render(request, 'blog/post_edit.html', {'form':form})

def post_detail(request,pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html',{'post':post})


# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
#     return render(request,'blog/post_list.html',{'posts':posts})
class PostListView(ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDeleteView(DeleteView):
	model = Post
	success_url=reverse_lazy('blog:post_list')

# class BookmarkDeleteView(DeleteView):
# 	model = Bookmark
# 	success_url=reverse_lazy('bookmark:list')

# Create your views here.
