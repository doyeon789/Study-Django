from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

# def new(request):
#     form = ArticleForm()
#     context = { 
#         'form' : form
#     }
#    return render(request, 'articles/new.html', context)

def create(request):
    # 사용자의 요청 방법에 따라서 조건 분기
    if request.method == 'POST':
        # 사용자가 넘겨준 데이터를 ModelForm class에 집어 넣으면
        # 필요한 field들의 정보를 알아서 가져와서 쓴다.
        form = ArticleForm(request.POST)
        #print(form)
        if form.is_valid(): #유효성 검사
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/new.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('articles:index')

# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(article)
#     context = {
#         'article': article,
#         'form': form
#     }
#     return render(request, 'articles/edit.html', context)


def update(request, pk):
    article= Article.objects.get(pk=pk)
    if request.method == 'POST':   
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else : 
        form = ArticleForm(instance=article)
    context = {
        'article':article,
        'form':form
    }
    return render(request, 'articles/edit.html',context)

