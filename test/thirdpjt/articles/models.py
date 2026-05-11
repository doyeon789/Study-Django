from django.db import models

# Create your models here.
# 게시글을 관리할 수 있는 어떤 객체를 저으이
    # 이 장고 모델을 위한 클래스 우리가 처음부터 전부 다 직접 정의하지 않는다.
    # 게시글 이라는 정보를 위해서 필요로 하는 기능들이 너무 많다.
    # 예를 들어, SQL? ㅡㅇㄹ 대신하는 파이썬 문법? 같은건? 어딨지?
    # 그리고, 게시글을 저장? 하는 방법? 같은건 어딨지?
    # 게시글의 각 특징(제목, 내용, 등등)을 저장하려면 정상적인 데이터인지 아닌지 어떻게 확인하지?
# models.Model클래스 상속
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''
            사람이 보기 좋게 출력 형태를 정의
        '''
        return self.title