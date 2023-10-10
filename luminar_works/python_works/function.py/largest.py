num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))
def largest(a,b,c):
    if a>b and a>c:
        print("largest number is",a)
    elif b>a and b>c:
        print("largest number is",b)
    else:
        print("largest number is",c)

largest(num1,num2,num3)               
