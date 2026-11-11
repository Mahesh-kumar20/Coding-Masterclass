n = int(input("Enter number: "))

num = n + 1

while True:
    is_prime = True

    if num <= 1:
        is_prime = False
    else:
        i = 2

        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1

    if is_prime:
        print("Next Prime:", num)
        break

    num += 1
