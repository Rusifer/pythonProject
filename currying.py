# Currying
# 여러개의 인자를 받는 함수로부터 일부(1개) 인자만 받아서 나머지 인자를 받는 다른 함수를 만들어 낸다
def add(num1, num2):
  return num1 + num2

def curry(func, var):
  y = var
  def f(x):
    return func(x, y)
  return f

def add_curry(x):
  return (lambda y : x + y)

print(add_curry(2)(3))