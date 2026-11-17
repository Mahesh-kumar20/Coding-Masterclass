n = int(input("Enter number: "))

max_terms = 0
best_start = 1

for i in range(1, n + 1):
    num = i
    count = 1

    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1

        count += 1

    if count > max_terms:
        max_terms = count
        best_start = i

print("Start =", best_start)
print("Terms =", max_terms)