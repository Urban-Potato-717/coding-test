#* 독립된 if
#* 세 조건이 모두 True이므로 세 문장이 모두 출력된다.
number = 5

if number < 1000:  # True
    print("1000보다 작다")

if number < 100:   # True
    print("100보다 작다")

if number < 10:    # True
    print("10보다 작다")

#* if-elif
#* 위에서부터 확인하다 **처음 True인 조건 하나만** 실행하고 끝남.
number = 5

if number < 1000:       # True → 실행
    print("1000보다 작다")
elif number < 100:
    print("100보다 작다")
elif number < 10:
    print("10보다 작다")