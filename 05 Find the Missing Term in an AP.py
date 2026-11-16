arr = [2, 5, 11, 14, 17]

diff = min(abs(arr[i+1] - arr[i]) for i in range(len(arr)-1))

for i in range(len(arr)-1):
    if abs(arr[i+1] - arr[i]) == 2 * diff:
        missing = arr[i] + (arr[i+1] - arr[i]) // 2
        print("Missing number:", missing)
        break