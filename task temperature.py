"""
Author : S Tippu Sahib
Date: 25-10-2024

Description:Write a Python program to convert temperature values back and forth between Celsius and Fahrenheit. The user should be able to input a temperature in Celsius or Fahrenheit, and the program should convert it to the other unit using the formula:
c/5=f−32/9

    For Celsius to Fahrenheit conversion:
    f=(9/5×c)+32

    For Fahrenheit to Celsius conversion:
    c=5/9×(f−32)
"""

temperature= int(input("Enter temperature:"))
scale = input("Is this (C)elsius or (F)ahrenheit? ")
if scale=='C':
    result_c = (9/5 * temperature)+32
    print(temperature , "Celsius is ",result_c,"Fahrenheit")
else :
    result_f = 5/9 *(temperature - 32)
    print(temperature, "Fahrenheit is" ,result_f , "Celsius" )