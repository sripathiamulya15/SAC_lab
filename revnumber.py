#reverse a number
a=int(input("Enter a number to be reversed:"))
rev=0
temp=a
while temp>0:
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10
print(f"The reversed number for {a} is {rev}")
