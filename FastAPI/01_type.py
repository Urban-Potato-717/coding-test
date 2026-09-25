# "타입 힌트"
# 함수 매게변수인 first_name, second_name 이 부분을
# first_name: str, second_name: str 로 바꾼다.
def get_full_name(first_name: str, second_name: str):
    full_name = first_name.capitalize() + " " + second_name.title()
    # 뭐가 엄청 크게 바뀌지는 않지만, crtl + space 로 자동완성 트리거 시 더욱 다양한 옵션이 출력됨.

    return full_name

print(get_full_name("john", "doe"))

# 에디터가 변수의 타입을 알고 있기 때문에 자동완성 뿐만아니라 오류도 검사할 수 있다.
# mypy 확장자 사용
def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age

# "타입 선언"
# str뿐 아니라 모든 파이썬 표준 타입을 선언할 수 있다.
def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_e

# typing 모듈
# 표준 라이브러리의 typing 모듈에서 무언가를 import해야 할 수 있다.
# 예를 들면 어떤 값이 "아무 타입"일 수 있다고 선언하려면, typing의 Any를 사용할 수 있다.
from typing import Any

def some_function(data: Any):
    print(data)

# Generic(제네릭) 타입
# 일부 타입은 대괗호 안에 "타입 매개변수"를 받아 **내부 타입을 정의**할 수 있다. 
# 예를 들어 "문자열의 리스트"는 list[str]로 선언한다.

## List
# str의 list인 변수를 정의해보자.
def process_items(items: list[str]):
    for item in items:
        print(items)