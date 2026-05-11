from django.shortcuts import render

# Create your views here.
def index(request):
    name = 'jayden'
    # 쿼리문을 작성해요. 디비에서 데이터를 가져온다. 
    company = 'ssafy'
    context = {
        'name': name,
        'company': company
    }
    return render(request, 'articles/index.html', context)

import random
def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육']
    picked = random.choice(foods)
    context = {
        'foods': foods,
        'picked': picked
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
        'message': message
    }

    return render(request, 'articles/catch.html', context)


def detail(request, numm):
    context = {
        "article_id": numm
    }
    # num을 이용해서 데이터베이스에 조회
    # 그 결과를 context에 담아서 건네주면 게시글 정보 활용
    return render(request, 'articles/detail.html', context)


def get_company_list(request):
    people_list = [
        {'company': 'samsung', 'name': '김씨'},
        {'company': 'ssafy', 'name': '이씨'}
    ]
    context = {
        'people_list': people_list
    }
    return render(request, 'articles/company_list.html', context)


def intro_company(request, company, name):
    context = {
        'company': company,
        'name': name
    }
    return render(request, 'articles/intro_company.html', context)