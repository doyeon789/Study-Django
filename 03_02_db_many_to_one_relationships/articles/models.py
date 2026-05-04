from django.db import models

from django.conf import settings

# Create your models here.
class Article(models.Model):
    
    # 여기서 User 클래스를 직접 작성하지않는다.
    # 왜냐하면 Article 클래스가 실행될때 User 클래스가 존재하지 않을수도 있기 때문
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 'accounts.User' 라는 문자열만 들고 있다가, 나중에 모든 모델이 
    # 다 로드된 이후에 진짜 User클래스르 ㄹ찾아서 연결
    # ==> '지연 평가'
    # 지연 평가는 ORM에서도 쓰임. Article.objects.all() 자체는 DB에 요청을 보내지 않음
    # 언제 요청을 보내냐면, list()형태로 형변환을 하거나 for로 반복하거나, 실제 데이터를 활용할때  평가를 진행
    # 효율 및 최적화를 위해
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    # 외래 키는 필드 어디에 두어도 실제 테이블에서는 마지막에 위치함
    # 외래 키 이름을 이렇게 상대방 클래스 이름으로 지은 이유
    # django가 최종적으로 설계도를 만들때 외래 키 필드 이름에 _id를 자동으로 붙이기 때문
    # 외래 키 이름을 단수형으로 지은 이유는
    #   N에서 1을 참조하는 것을 명시하기 위함.
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


