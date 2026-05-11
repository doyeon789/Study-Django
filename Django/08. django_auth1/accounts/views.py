from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login


# Create your views here.
def login(request):
    if request.method == 'POST':
        '''
            login -> sessino을 생성해 달라는 POST
            그런데, 현재 사용자가 request.POST에 담아 보낸 데이터는
            사실 그 생성할 session에는 저장되지 않을 데이터
            그래서 AuthenticationForm은 ModelForm이 아님!
                그말은 유효성 검사가 끝나고 난 뒤에도 save()를 할게 아님
                '로그인'이라는 행위를 할 것임
                그 로그인 이라는 행위가 session 생성하는 것
        '''
        form  = AuthenticationForm(request, request.POST)
        #form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 세션을 생성한다.
            # 세션 id를 가지고 사용자에게 cookie에 담아서 보낸다.
            auth_login(request, form.get_user())
            return redirect('articles:index') 
    else:
        form = AuthenticationForm
    context = {
        'forms':form
    }
    return render(request, 'accounts/login.html', context)