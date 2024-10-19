'''
Author= S Tippu Sahib
Date: 19-10-2024
Description: Simple desktop calculator using Python. Only the five basic arithmetic operators.

'''
num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))
sum=num1+num2
print("the sum of num1 and num2 is",sum)
subtract=num3-num1
print("the difference when num3 is subtracted from num1 is",subtract)
multiply=num2*num3
print("the product of num3 and num2 is",multiply)
divide=num1/num3
print("the quotient when num1 is divided by num3 is",divide)
modulus=num1%num2
print("The remainder when num1 is divided by num2 is",modulus)
result=(num1 + num2) * num3 / 2
print("The result of (num1 + num2) * num3 / 2 is: result",result)