#sum of digits
num=int(input("Enter your number:"))
sum=0
temp=num
while temp>0:
    rem=temp%10
    sum+=rem
    temp=temp//10
print(f"The sum of digits in {num} is {sum}")
