from django.shortcuts import render

# Create our views here
# django에서 view함수를 만들때느는 항상
# 첫번째 인자로 request를 저으이
#   이 reqest 인자에 사용자의 요청정보가 모두 포함되어 있다.
#   
def index(request):
    # reder(request, template의 경로)
    # templates/ <- 요거 생략하고 작성
    # app_name/templates/app_name
    return render(request, 'articles/index.html')