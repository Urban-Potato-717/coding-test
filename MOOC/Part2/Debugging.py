"""MOOC Part 2: Debugging.

학습 목표:
- 실패한 입력을 고정해 문제를 반복해서 재현한다.
- 변수와 조건식의 값을 출력해 오류 범위를 좁힌다.
- 계산 결과를 변수에 다시 저장해야 값이 바뀐다는 것을 확인한다.

관련 노트:
- notes/Debugging.md
"""


def calculate_daily_wages(hourly_wage, hours, day):
    """일요일에는 두 배로 계산한 일급을 반환한다."""
    daily_wages = hourly_wage * hours

    if day == "Sunday":
        daily_wages *= 2

    return daily_wages


def run_debug_example():
    """강의의 실패 입력으로 중간 값을 관찰한다."""
    hourly_wage = 20.0
    hours = 6
    day = "Sunday"

    daily_wages = hourly_wage * hours
    print("condition:", day == "Sunday")
    print("wages before:", daily_wages)

    if day == "Sunday":
        daily_wages *= 2

    print("wages after:", daily_wages)
    print(f"Daily wages: {daily_wages} euros")


if __name__ == "__main__":
    run_debug_example()
