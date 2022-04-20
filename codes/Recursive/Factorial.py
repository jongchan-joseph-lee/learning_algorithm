# 팩토리얼 출력 문제 

def factorial(N):
  if (N>1) & (N<=12):
    return N*factorial(N-1)
  else:
    return 1

  

a = int(input()) 

print(factorial(a))
