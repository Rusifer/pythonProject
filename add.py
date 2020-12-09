#  고계함수
# 함수를 인자로 받거나 함수를 리턴하는 함수 

import math

def calc(num1, num2, op):
  return op(num1, num2)

def add(num1, num2):
  return num1 + num2

def multiply(num1, num2):
  return num1 * num2

def power(num1, num2):
  return math.pow(num2, num1)

t = calc(2, 3, add)
print(t)

def calcWith2(op):
 return lambda num : op(2,num)

add2 = calcWith2(add)
print(add2(3))

calcWith3 = lambda op : lambda num : op(2, num)

add2 = calcWith2(multiply)
print(add2(3))
