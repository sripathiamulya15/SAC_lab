#greatest of 3 numbers
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a==b==c :
    print("All the values are equal")
elif a>=b or a>=c:
    print(f"{a} is the greatest number")
elif b>=c or b>=a:
    print(f"{b} is the greatest number")
else:
    print(f"{c} is the greatest number")
