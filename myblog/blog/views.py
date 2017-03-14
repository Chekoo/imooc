#coding=utf-8
from django.shortcuts import render
from . import models

def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})

def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})

def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})

def edit_action(request):
    title = request.POST.get('title', 'TITLE')    #括号内第二个参数为默认值，以防止抛异常
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', '0')
    if article_id == '0':   #id若为0，则为创建新文章
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})
    #id不为0，则修改文章，将新的数据进行赋值并保存
    article = models.Article.objects.get(pk=article_id)
    article.title = title    #进行赋值
    article.content = content
    article.save()      #保存
    return render(request, 'blog/article_page.html', {'article': article})