from rest_framework import serializers
from .models import Article, Comment


# 단일 게시글 데이터(단일 인스턴스)를 직렬화 하는 도구
# 그러면 ArticleListSerializer를 단일 게시글에서는 못쓰나요? ==> NO
class ArticleSerializer(serializers.ModelSerializer):
     # 단ㅇ리 게시글 + 댓글 목록 조회를 위해 댓글 목록 직렬화 도구를 작성
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id','content')

    # 기존에 article이 가지고 있는 역착점 매니저인 comment_set을 값을 CommentDetailSerialiser의 잿글 결과 목록으로 재정의
    # [참고] 모델에서 외래키 필드에서 related_name 설정 값ㅇ르 바꿔서 comment_set 역참조 이름을 변경할 수 있음
    comment_set = CommentDetailSerializer(many=True, read_only = True)
    
    # 완전히 새ㅗㄹ운 필드를 선언 (댓글의 개수)
    num_of_comments = serializers.SerializerMethodField()


    class Meta:
        model = Article
        fields = '__all__'

    # 위에서 추가한 num_of_comments 필드의 값ㅇ르 변호낳나느 메서드 정의
    def get_num_of_comments(self, obj):
        # 여기서 obj는 Serializer가 처리하는 Article 인스턴스
        # view에서 annotate 한 필드를 그대로 사용 가능
        return obj.num_of_comments
    
        # 만약에 view에서 annotate를 사용하지 않았다면,
        # num_of_comments = obj.comment_set.count()
        # return self.num_of_comments


# 전체 게시글 데이터(쿼리셋)를 직렬화 하는 도구
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


class CommentSerializer(serializers.ModelSerializer):

    # [댓글 데이터 제공할 때 댓글이 작성된 게시글의 번호화 제목도 함께 제공하기 위한 추가 데이터 설정]
    # 게시글의 제목을 직렬화 할 수 있는 도구 생성
    class AritlcleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('id','title',)

    # 기존 읽기전용 필드인 article 필드를 위해 도구(ArticleSerializer)의 결과 값으로 재정의
    # 기존 필드를 재정의할때는 Meta 클래스에서 작성했던 read_only_fields가 먹히지 않게 됨
    # 더룬 방법으로 읽기 전용 필드로 설정
    article = AritlcleTitleSerializer(read_only = True)

    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('article',)
