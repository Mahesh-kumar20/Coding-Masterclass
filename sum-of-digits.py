n=int(input("enter number:"))
sign = 1
if n < 0:
  sign = -1
  n=abs(n)
sum = 0
while n>0:
  digit = n % 10
  sum = sum + digit
  n=n//10
print(sum)