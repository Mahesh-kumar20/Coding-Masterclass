n=int(input("enter number: "))

original = n
reverse = 0

while n>0:
    digit=n%10
    reverse= reverse * 10 + digit
    n=n//10
    
if reverse == original:
    print("palindrome")
elif reverse != original:
    print("not palindrome")
