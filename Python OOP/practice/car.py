"""Car 클래스 실습용 모듈.

학습 목표:
- __init__에서 받은 값을 인스턴스 변수에 저장한다.
- 메서드의 self가 현재 메서드를 호출한 객체를 가리키는지 확인한다.

관련 노트:
- notes/Self_InstanceVariable.md
"""


class Car:
    """자동차의 상태와 동작을 표현한다."""

    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")
