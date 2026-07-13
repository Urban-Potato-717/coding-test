"""Python 기초 연습 B1~B3.

학습 기록:
- B1: 나머지로 홀짝을 판단한다.
- B2: 0을 종료 신호로 사용하고, 종료 값은 합계와 개수에서 제외한다.
- B3: 문자열을 직접 순회하며 모음의 개수를 센다.

복습 질문:
- B2에서 0인지 검사하기 전에 합계에 더하면 어떤 문제가 생기는가?
- 여러 elif 대신 모음 문자열과 in을 사용할 수 있는가?
"""


def is_even(integer):
    """정수가 짝수인지 반환한다."""
    return integer % 2 == 0


def read_numbers_until_zero():
    """0을 입력할 때까지 입력된 수의 합계와 개수를 반환한다."""
    total = 0
    count = 0

    while True:
        number = int(input("number: "))
        if number == 0:
            break

        total += number
        count += 1

    return total, count


def count_vowels(text):
    """영문 소문자 문자열에 포함된 모음의 개수를 반환한다."""
    count = 0

    for character in text:
        if character in "aeiou":
            count += 1

    return count
