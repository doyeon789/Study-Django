# articles/forms.py
from django import forms
from .models import Article

# ModelForm 예시
class ArticleForm(forms.ModelForm):
    # 이 Form 클래스를 정의하기 위해 필요한 데이터
    # 즉, 나를 위한 나에 대한 데이터
    # 메타 데이ㅓㅌ
    class Meta:
        # 이 Form을 구성하기 위해 필요한 정보
        #  -> 어떤 모델?
        model = Article
        #  -> 그 모델이 가진 어떤 필드로 form을 구성할꺼야?
        fields = '__all__'
        # fields = ['title', 'content', ]
        # exclude = ('title',)

# 게시글 작성을 위해 필요한 form을 어떻게 구성할ㅈ;ㅣ
# 미리 정리해 두는 클래스
# class ArticleForm(forms):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)