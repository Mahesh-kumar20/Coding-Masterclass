n=int(input("Enter an integer: "))
sign = 1
if n < 0:
  sign = -1
n= abs(n)
reverse = 0
while n>0:
 
  digit =n % 10
  reverse =reverse * 10 + digit
  n=n//10
reverse = reverse * sign
print(reverse)
