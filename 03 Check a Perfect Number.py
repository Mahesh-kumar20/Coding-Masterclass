n=int(input("enter number: "))
count = 0
for i in range (1,n):
  if n % i == 0:
    count += i
if count==n:
  print("perfect number")
else:
  print("not perfect number")