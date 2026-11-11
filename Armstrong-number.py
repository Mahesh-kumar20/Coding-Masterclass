n=int(input("enter number:"))
original = n
temp=n
count = 0
total =0

while temp > 0:
  count +=1
  temp =temp // 10
if n==0:
    count = 1

temp = n
while temp>0:
    digit =temp % 10
    total += digit ** count
    temp =temp // 10
if total == original:
    print("Armstrong number")
else:
    print("not armstrong number")