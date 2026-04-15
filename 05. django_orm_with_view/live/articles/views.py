from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
# 게시글 전체 조회 -> QuerySet API
# template
def index(request):
    # articles = [{title: 'title', content: 'content'}]
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article()
    article.title = title
    article.content = content
    article.save()
    return redirect('articles:index')
    # return render(request, 'articles/create.html')


def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')