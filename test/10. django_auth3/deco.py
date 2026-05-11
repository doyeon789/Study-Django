# ============================================================
# 파이썬 함수 데코레이터(Decorator) 예제
# ============================================================

# 1. 데코레이터란?
#    함수를 인자로 받아 기능을 추가한 새 함수를 반환하는 함수.
#    @구문을 사용해 기존 함수를 수정하지 않고 동작을 확장할 수 있다.


# ── 기본 구조 ────────────────────────────────────────────────

def my_decorator(func):
    """가장 단순한 데코레이터 뼈대"""
    def wrapper(*args, **kwargs):
        print("[before] 함수 실행 전")
        result = func(*args, **kwargs)        # 원래 함수 호출
        print("[after]  함수 실행 후")
        return result
    return wrapper


@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")


# say_hello("Alice") 는 내부적으로 my_decorator(say_hello)("Alice") 와 동일
say_hello("Alice")
print()