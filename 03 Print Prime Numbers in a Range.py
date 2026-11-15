L=int(input("enter L:"))
U=int(input("enter U:"))
for i in range(L,U+1):
  if(i>1):
    for j in range(2,i):
      if(i%j==0):
        break
    else:
      print(i)