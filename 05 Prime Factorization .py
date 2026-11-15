n = int(input("Enter number: "))

i = 2

while n > 1:
    if n % i == 0:
        print(i, end=" ")
        n = n // i
    else:
        i = i + 1