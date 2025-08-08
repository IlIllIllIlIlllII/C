a=int(input())
b=int(input())
a1=1
sum=0
k=1
while b>=1:

  i=b%10
  b=b//10
  a1=a*i
  print(a1)
  sum+=a1*k
  k*=10
print(sum)
