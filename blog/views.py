from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension

from .models import Category, Tag, Post

import markdown
import re


# Create your views here.


def index1(request):
    return HttpResponse('欢迎访问我的博客首页')


def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={
        'title': '我的博客主页',
        'welcome': '欢迎访问我的博客首页',
        'post_list': post_list
    })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',  # 基本扩展
        'markdown.extensions.fenced_code',  # 语法高亮
        TocExtension(slugify=slugify),  # 允许自动生成目录
    ])
    post.body = md.convert(post.body)
    # 空目录不处理
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    # 动态添加属性，动态语言的好处
    post.toc = m.group(1) if m is not None else ''
    return render(request, 'blog/detail.html', context={
        'post': post
    })


def archive(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    )
    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })


def tag(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t)
    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })