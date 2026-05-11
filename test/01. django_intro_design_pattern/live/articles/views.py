from django.shortcuts import render
import random
# Create our views here
# django에서 view함수를 만들때느는 항상
# 첫번째 인자로 request를 저으이
#   이 reqest 인자에 사용자의 요청정보가 모두 포함되어 있다.
#   
def index(request):
    name = 'doyeon'
    context = {
        'name' : name
    }
    return render(request, 'articles/index.html', context)

def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육']
    picked = random.choice(foods)
    context = {
        'foods' : foods,
        'picked' : picked
    }
    return render(request, 'articles/dinner.html', context)

def search(request):
    return render(request, 'articles/search.html')

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    # 이 함수가 throw에서 건네는 데이터를 받는 역할

    message = request.GET.get('message')
    context = {
        'message' : message
    }

    return render(request, 'articles/catch.html', context)

def detail(request, num):
    context = {
        'article_id':num
    }
    return render(request, 'articles/detail.html',context)

def get_company_list(request):
    people_list = [
        {'company':'samsung','name':'doyeon'},
        {'company':'ssafy','name':'dodododo'}
    ]
    context = {
        'people_list' : people_list
    }
    return render(request, 'articles/intro_company.html', context)


def intro_company(request, company, name):
    context = {
        'company' : company,
        'name' : name
    }

    return render(request, 'articles/company.html', context)