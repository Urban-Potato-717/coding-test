'''
operator precedence 때문에 틀림. ~ / 2*a로 작성하면
(~ / 2) * a  <- 틀린 계산이 되니, 당연히 괄호를 쳐야 함.
'''
# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5
a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

x1 = (-b + sqrt(b**2 - (4*a*c))) / (2*a)
x2 = (-b - sqrt(b**2 - (4*a*c))) / (2*a)
print(f"The roots are {x1} and {x2}")