"""
TASK 1
Author: S TIPPU SAHIB
Date: 25-10-2024
Description:Write a Python program to convert temperature values back and forth between Celsius
and Fahrenheit. The user should be able to input a temperature in Celsius or Fahrenheit,
and the program should convert it to the other unit.
"""
number_1 = int(input("Enter first number:"))
number_2 = int(input("Enter second number:"))
number_3 = int(input("Enter third number:"))
if number_1>number_2 and number_1>number_3:
    print("The largest number is :", number_1)
elif number_2>number_1 and number_2>number_3:
    print("The largest number is :", number_2)
else:
    print("The largest number is:" , number_3)


