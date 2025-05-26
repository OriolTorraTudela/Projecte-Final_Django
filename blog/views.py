from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag

def index(request):
    latest = Post.objects.order_by('-date')[:3]
    return render(request, 'index.html', {'posts': latest})

def post_list(request):
    posts = Post.objects.order_by('-date')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', {'post': post})

def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'authors_list.html', {'authors': authors})

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'author_detail.html', {'author': author})

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'tag_list.html', {'tags': tags})

def tag_posts(request, tag):
    tag_obj = get_object_or_404(Tag, tag=tag)
    posts = tag_obj.posts.order_by('-date')
    return render(request, 'tag_post.html', {'tag': tag_obj, 'posts': posts})

def custom_404(request, exception):
    return render(request, '404.html', status=404)
