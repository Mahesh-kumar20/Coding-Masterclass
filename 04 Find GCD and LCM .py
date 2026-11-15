a=int(input("enter a:"))
b=int(input("enter b:"))
x=a
y=b

while b!=0:
  r=a%b
  a=b
  b=r
print("GCD:",a)
print("LCM:",(x*y)//a)

 