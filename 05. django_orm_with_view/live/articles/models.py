from django.db import models

# Create your models here.
class Article(models.Model):
    # 제목, 내용, 생성 일자, 수정 일자.
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)