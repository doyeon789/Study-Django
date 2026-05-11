from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    # 외래키는 필드 어디에 두어도 실제 테이블에서는 마지막에 위치한다.
    # 외래키 이름을 지을때 상대방 클래스 이름으로 지은 이유:
        # django가 최종적으로 설계도를 만들때 외래키 필드에 '_id'를 자동을 붙여주기 때문에
    # 외래키 이름을 단수형으로 지은 이유:
        # N에서 1을 참조한 다는것을 명시하기 위해서
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
