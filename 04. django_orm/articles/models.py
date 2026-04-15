from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    upated_at = models.DateTimeField(auto_now=True)

'''객체 전체 조회
articles = Article.objects.all()
'''

'''객체 생성 1
article = Article()
article.title = 'first'
article.content = 'django!'
article.save()
'''

'''객체 생성 2
article = Article(title='second', content='hello!')
article.save()
'''

'''객체 생성 3
Article.objects.create(title='third', content='django!')
'''

'''객체 필터 조회
Article.objects.filter(content='django!')
Article.objects.filter(title='abc!')
Article.objects.get(title='first')
'''

'''객체 단일 조회
Article.objects.get(pk=1)
# Article.objects.get(content='django!')
# 다수 객체 조회시 오류 발생
'''

'''객체 데이터 수정
article = Article.objects.get(pk=1)
article.title = 'updated'
article.save()
'''

'''객체 삭제
article = Article.objects.get(pk=1)
article.delete()
'''

