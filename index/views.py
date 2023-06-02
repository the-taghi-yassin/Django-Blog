from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import CreateView
from taggit.models import Tag
from django.db.models import Q
from .models import *
from .forms import *


def home(request):
    cats = Category.objects.all().order_by('-id')
    post = Post.newmanager.all().order_by('-id')
    paginator= Paginator(post,12)
    page_num = request.GET.get('page',1)
    post= paginator.page(page_num)
    return render(request,'home.html',{'post':post, 'cats':cats})


class AddCourseView(CreateView):
    model = Post
    template_name = 'add.html'
    form_class = PostForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddCourseView, self).form_valid(form)
    def test_func(self):
        return self.request.user.is_superuser

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    cats = Category.objects.all().order_by('-id')
    fav = bool
    if post.favourites.filter(id=request.user.id).exists():
        fav = True
    return render(request,'detail.html',{'post':post, 'cats':cats, 'fav': fav})

def category(request):
    cats = Category.objects.all().order_by('-id')
    return render(request,'category_mobi.html',{'cats':cats})

def category_post(request, slug):
    category = Category.objects.get(slug=slug)
    cats = Category.objects.all().order_by('-id')
    post = Post.newmanager.filter(category=category).order_by('-id')
    paginator= Paginator(post,6)
    page_num = request.GET.get('page',1)
    post= paginator.page(page_num)
    return render(request, 'category_post.html',{'post':post,'cats':cats})

def categories(request):
    cats = Category.objects.all().order_by('-id')
    catid = request.GET.get('categories')
    if catid:
        post = Post.newmanager.filter(category=catid).order_by('-id')
        paginator= Paginator(post,12)
        page_num = request.GET.get('page',1)
        post= paginator.page(page_num)
    else:
        post = Post.newmanager.filter(status='published').order_by('-id')
        paginator= Paginator(post,12)
        page_num = request.GET.get('page',1)
        post= paginator.page(page_num)
    return render(request,'categories.html',{'cats':cats, 'post':post,'catid':catid})

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q=request.GET['q']
        post= Post.newmanager.filter(Q(title__icontains=q)| Q(description__icontains=q)| Q(content__icontains=q)| Q(book_author__icontains=q)).order_by('-id')
        paginator= Paginator(post,12)
        page_num = request.GET.get('page',1)
        post= paginator.page(page_num)
    else:
        post= Post.newmanager.all().order_by('-id')
    paginator= Paginator(post,12)
    page_num = request.GET.get('page',1)
    post= paginator.page(page_num)
    return render(request,'search.html',{'post':post,'q':q})


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = Post.tags.most_common()[:4]
    posts = Post.newmanager.filter(tags=tag)
    context = {
        'tag':tag,
        'common_tags':common_tags,
        'posts':posts,
    }
    return render(request, 'tags.html', context)