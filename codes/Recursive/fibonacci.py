# 피보나치수열 출력 문제
def fibo(x):

  if (x==1):
    return 1

  if (x==0):
    return 0
  
  if (x>=2):
    return fibo(x-1) + fibo (x-2)



a = int(input())

print(fibo(a))
